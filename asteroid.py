import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Create a surface large enough for the circle
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        # Draw the circle onto self.image
        pygame.draw.circle(self.image, "white", (radius, radius), radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position