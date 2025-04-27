# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from constants import *

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        #player.draw(screen)
        #player.update(dt)

        updatable.update(dt)

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()