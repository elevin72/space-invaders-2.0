import pygame 
import os
import random
import time

# font intializer
pygame.font.init()
# Window data
WIDTH, HEIGHT = (750, 750)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders 2.0")

# Load ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# lasers
R_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
B_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
G_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
Y_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# dict with colors
colors = {
            "red" : (RED_SPACE_SHIP, R_LASER),
            "blue" : (BLUE_SPACE_SHIP, B_LASER),
            "green" : (GREEN_SPACE_SHIP, G_LASER)
}

# ship class for game
class Ship():
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down = 0
    
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = Y_LASER

class Enemy(Ship):
    def __init__(self, x, y, health=100, color=["red", "green", "blue"]):
        super().__init__(x, y, health)
        self.color = color[random.randrange(0,3)]
        self.ship_img, self.laser_img = colors.get(self.color)

        


# main procedure
def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 35)
    ship = Player(300, 650)
    enemy = Enemy(100, 200)
    enemy2 = Enemy(200, 200)
    velocity = 15
    

    def redraw_window():
        WIN.blit(BG, (0,0))
        ship.draw(WIN)
        enemy.draw(WIN)
        enemy2.draw(WIN)
        lives_label = main_font.render(f"Lives Remaining : {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level {level}", 1, (255,255,255))
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width()-10,10))        

        pygame.display.update()       


    while run:        
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: # left key press
            ship.x -= velocity
        if keys[pygame.K_RIGHT]: # right key press
            ship.x += velocity
        if keys[pygame.K_UP]: # up key press
            ship.y -= velocity
        if keys[pygame.K_DOWN]: # down key press
            ship.y += velocity

main()
