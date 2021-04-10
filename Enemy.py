from Ship import *
from Laser import *
class Enemy(Ship):
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img =color
        self.mask = pygame.mask.from_surface(self.ship_img)     

    def move(self, vel):
        self.y += vel
        
    # def fire(self, enemy_lasers):
    #     enemy_lasers.append(Laser(self.x-4,self.y, self.laser_img, 10))
