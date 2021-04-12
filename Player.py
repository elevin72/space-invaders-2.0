from Ship import *
from Laser import *
from timeit import default_timer as timer

class Player(Ship):
    def __init__(self, x, y, img, lives=3, health=100):
        super().__init__(x, y, health)
        self.ship_img = img[0]
        self.laser_img = img[1]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.lives = lives
        self.max_health = health   
        self.cool_down_timer = 0
        self.x2_timer = 10000000000
        self.lasers = []

    def move_lasers(self):
        for laser in self.lasers:
            laser.y -= laser.velocity

    def __fire(self, offset=0):
        self.lasers.append(Laser(self.x + offset, self.y, self.laser_img, 10))

    def fire(self):
        x2 = timer()
        if self.x2_timer - x2 < 5:
            self.__fire(offset=-8)
            self.__fire(offset=8)
        else:
            self.__fire()
        self.cool_down_timer = timer()

    def can_fire(self):
        end = timer()
        if (end - self.cool_down_timer < 0.5):
            return False
        else:
            return True

    def handle_powerup(self, powerup):
        if powerup.kind == "heart":
            self.lives += 1
        if powerup.kind == "x2":
            self.x2_timer = timer()
        if powerup.kind == "bomb":
            # TBD
            pass

            
            
           

















