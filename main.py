import pygame
import constants
from player import *
from constants import *
from astereoid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape

def main():
    pygame.init()
    clock=pygame.time.Clock()
    dt=0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
   
    Player.containers = (drawable, updatable)
    Asteroid.containers=(asteroids,drawable,updatable)
    AsteroidField.containers=(updatable)
    
    kivi_kentta= AsteroidField()
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
        for piirra in drawable:            
            piirra.draw(screen)
        updatable.update(dt)
        for collision in asteroids:
            if collision.collision(pelajaa) == True:
                print("Game over!")
                exit()
        pygame.display.flip()
        dt=clock.tick(60)/1000
        

if __name__ == "__main__":
    main()