import pygame
import os
from Enemy import *
from Player import *
from GameObject import *
from Context import *

class Laser(GameObject): 

    # always import Game before this class so convert_alpha works properly()
    # import it yourself?
    colors = {
        "red" : pygame.image.load(os.path.join("assets", "pixel_laser_red.png")).convert_alpha(),
        "blue" : pygame.image.load(os.path.join("assets", "pixel_laser_blue.png")).convert_alpha(),
        "green" : pygame.image.load(os.path.join("assets", "pixel_laser_green.png")).convert_alpha(),
        "yellow" : pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png")).convert_alpha()
    }

    def __init__(self, x, y, velocity, color):
        super().__init__(x, y, velocity)
        self.color = color
        self.img = self.colors[color]
        self.mask = pygame.mask.from_surface(self.img)
        
    def move(self):
        # covers both enemy and player lasers
        if self.y > HEIGHT or self.y < -15:
            ctx.lasers.remove(self)
        self.y += self.velocity

    def draw(self):
        WIN.blit(self.img, (self.x, self.y))
