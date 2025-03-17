import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position+=self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        kulma = random.uniform(20,50)
        uusi_1 = self.velocity.rotate(kulma)
        uusi_2 = self.velocity.rotate(-kulma)
        uusi_radius = self.radius-ASTEROID_MIN_RADIUS
        asteri = Asteroid(self.position.x,self.position.y,uusi_radius)
        obelix = Asteroid(self.position.x,self.position.y,uusi_radius)
        asteri.velocity=uusi_1*1.2
        obelix.velocity=uusi_2*1.2 

