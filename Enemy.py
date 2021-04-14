from Player import *
from Powerup import *
from Ship import *
from Laser import *

class Enemy(Ship):
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

    def move(self, velocity):
        if self.y > HEIGHT+50:
            ctx.enemies.remove(self)
            ctx.player.lives -= 1
        self.y += velocity

    def fire(self):
        ctx.lasers.append(Laser(self.x-4,self.y, self.color, 10))



