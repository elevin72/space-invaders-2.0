import random
from GameObject import *
from Player import *

class Powerup(GameObject):

    kinds = {
        "heart" : pygame.image.load(os.path.join("assets", "heart.png")).convert_alpha(),
        "x2" : pygame.image.load(os.path.join("assets", "x2.png")).convert_alpha(),
        "bomb" : pygame.image.load(os.path.join("assets", "bomb.png")).convert_alpha(),
        "explode" : pygame.transform.scale(pygame.image.load(os.path.join("assets", "explode.png")).convert_alpha(), (200,200))
        }
    def __init__(self, x, y, velocity=1, kind=None):
        super().__init__(x, y, velocity)
        if kind == None:
            kind = random.choice(["heart", "x2", "bomb"])
        if kind in self.kinds:
            self.kind = kind
            self.img = self.kinds[kind]
        else:
            exit()
            # throw something
            # powerup kind not supported
        self.mask = pygame.mask.from_surface(self.img)

    def explode(self, img):
        self.velocity = 0
        self.kind = "exploding"
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

