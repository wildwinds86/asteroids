# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from shots import Shot
from constants import *

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for a in asteroids:
            if a.is_colliding(player):
                print("Game over!")
                sys.exit()

            for s in shots:
                if a.is_colliding(s):
                    a.split()
                    s.kill()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()