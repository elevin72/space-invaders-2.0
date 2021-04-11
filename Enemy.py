from Ship import *
from Laser import *
class Enemy(Ship):
    # color dictionary
    colors = {
            "red" : (RED_SPACE_ship, R_LASER),
            "blue" : (BLUE_SPACE_ship, B_LASER),
            "green" : (GREEN_SPACE_ship, G_LASER)
            }
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.color = color
        self.ship_img, self.laser_img = self.colors[color]
        self.mask = pygame.mask.from_surface(self.ship_img)     

    def move(self, vel):
        self.y += vel
        
    # def fire(self, enemy_lasers):
    #     enemy_lasers.append(Laser(self.x-4,self.y, self.laser_img, 10))
