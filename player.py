from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
import pygame

from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        # Make the surface larger to accommodate rotation
        surface_size = int(PLAYER_RADIUS * 2 * 1.414)  # multiply by sqrt(2)
        self.image = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.rotation = 0
        self.redraw()
        self.shot_timer = 0
        self.shot_cooldown = 0.3

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def redraw(self):
        # Clear the surface
        self.image.fill((0,0,0,0))
        # Convert triangle points to surface coordinates
        local_points = [point - self.position + pygame.Vector2(self.rect.width/2, self.rect.height/2) for point in self.triangle()]
        # Draw on the surface
        pygame.draw.polygon(self.image, "white", local_points, width=2)

    def update(self, dt):
        # Keep existing update code
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.rect.center = self.position
        self.redraw()

        if self.shot_timer > 0:
            self.shot_timer -= dt

    def shoot(self):
        # Only shoot if timer is 0 or less
        if self.shot_timer <= 0:
            # Create and launch the shot
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            # Reset the timer to the cooldown value
            self.shot_timer = self.shot_cooldown

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]