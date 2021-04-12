import pygame

class Laser: 
    def __init__(self, x, y, img, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

        
