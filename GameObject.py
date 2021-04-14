import pygame
import os #imported for later use in inheritance tree
from Context import *

# Globals
WIDTH, HEIGHT = (750, 750)
# constant static thingys
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders 2.0")
# background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")).convert(), (WIDTH, HEIGHT)) 
ctx = Context(0)

# Interface for all game objects
class GameObject:
    # ctor
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.img = None
        self.mask = None

    ## all of these methods can be overidden ##
    def move(self):
        # This will move objects down for positive velocities
        self.y += self.velocity

    def draw(self):
        WIN.blit(self.img, (self.x, self.y))

    def update(self):
        self.move()
        self.draw()
            



