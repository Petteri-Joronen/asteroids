import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        self.position_x=x
        self.position_y=y
    def draw(self,):
        pygame.draw.circle(self,"white",(self.position_x,self.position_y),2)

    def update(self, dt):
        self.position+=self.velocity * dt 

