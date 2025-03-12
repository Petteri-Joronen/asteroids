import pygame
import constants
from player import *
from constants import *


def main():
    pygame.init()
    clock=pygame.time.Clock()
    dt=0
    pelajaa=Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pelajaa.draw(screen)
        pelajaa.update(dt)
        pygame.display.flip()
        dt=clock.tick(60)/1000
        

if __name__ == "__main__":
    main()