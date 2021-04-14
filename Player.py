from Ship import *
from Laser import *
from timeit import default_timer as timer

class Player(Ship):

    laser_img = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")).convert_alpha()
    img = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")).convert_alpha()

    def __init__(self, x, y, velocity, lives=3, health=100):
        super().__init__(x, y, velocity)
        self.mask = pygame.mask.from_surface(self.img)
        self.lives = lives
        self.health = health   
        self.cool_down_timer = 0
        self.x2_timer = 0
        self.lasers = []

    def move(self):
        self.y += self.velocity
        for laser in self.lasers:
            laser.y -= laser.velocity

    def draw(self):
        self.WIN.blit(self.img, (self.x, self.y))
        for laser in self.lasers:
            self.WIN.blit(self.laser_img, (laser.x, laser.y))

    def __fire(self, offset=0):
        self.lasers.append(Laser(self.x + offset, self.y, self.laser_img, 10))

    def fire(self):
        if timer() - self.x2_timer < 5:
            self.__fire(offset=-8)
            self.__fire(offset=8)
        else:
            self.__fire()
        self.cool_down_timer = timer()

    def can_fire(self):
        if (timer() - self.cool_down_timer < 0.5):
            return False
        else:
            return True

    def handle_powerup_collision(self, powerup):
        if powerup.kind == "heart":
            self.lives += 1
        if powerup.kind == "x2":
            self.x2_timer = timer()
        if powerup.kind == "bomb":
            self.lives -= 1

