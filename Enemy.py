from Ship import *
from Laser import *

class Enemy(Ship):
    lasers = []
    colors = {
            "red" : pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png")).convert_alpha(), 180),
            "blue" : pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png")).convert_alpha(), 180),
            "green" :pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png")).convert_alpha(), 180)
    }

    def __init__(self, x, y, velocity, color):
        super().__init__(x, y, velocity)
        self.color = color
        self.img = self.colors[color]
        self.mask = pygame.mask.from_surface(self.img)     

    def fire(self):
        self.lasers.append(Laser(self.x-4,self.y, self.color, 10))
