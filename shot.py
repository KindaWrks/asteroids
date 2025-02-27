import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        # Create a surface for the shot
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.redraw()

    def redraw(self):
        # Clear the surface
        self.image.fill((0, 0, 0, 0))
        # Draw the shot as a white circle
        pygame.draw.circle(self.image, "white", (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)

    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt
        # Update rect position
        self.rect.center = self.position