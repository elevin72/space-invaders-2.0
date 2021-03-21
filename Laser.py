import pygame
import os

R_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
B_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
G_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
Y_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

class Laser: 
    def __init__(self, x, y, img, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        
