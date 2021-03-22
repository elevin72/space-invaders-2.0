from Laser import *

RED_SPACE_ship = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png")), 180)
BLUE_SPACE_ship = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png")), 180)
GREEN_SPACE_ship = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png")), 180)
YELLOW_SPACE_ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))


# ship and laser classes for game
class Ship():
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
            
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()
    
    def fire(self, window):
        self.lasers.append(Laser(self.x, self.y, self.laser_img, 10))
        
    def move_lasers(self):
        for laser in self.lasers:
            laser.y += laser.velocity