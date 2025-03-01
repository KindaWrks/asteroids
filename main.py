import sys
import time

import pygame
from pygame.display import update

from shot import Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    SCORE = 0
    font = pygame.font.SysFont("Arial", 32)

    running = True
    while running:
        dt = clock.tick(60) / 1000  # Calculate dt first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # These should be outside the event loop
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                game_over_text = font.render("GAME OVER", True, (255, 255, 255))
                screen.blit(game_over_text, (550, 300))
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

                    if asteroid.radius <= ASTEROID_MIN_RADIUS:
                        SCORE += ASTEROID_SCORES['small']
                    elif asteroid.radius <= ASTEROID_MED_RADIUS:
                        SCORE += ASTEROID_SCORES['medium']
                    elif asteroid.radius <= ASTEROID_LARGE_RADIUS:
                        SCORE += ASTEROID_SCORES['large']
                    else:
                        SCORE += ASTEROID_SCORES['large']

        drawable.draw(screen)
        score_text = font.render(f"Score: {SCORE}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()



if __name__ == "__main__":
    main()
