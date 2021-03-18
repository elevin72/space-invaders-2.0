from Ship import *
from Laser import *

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_ship
        self.laser_img = Y_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health        

    def move_lasers(self):
        for laser in self.lasers:
            laser.y -= laser.velocity