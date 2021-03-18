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
RED_SPACE_ship = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png")), 180)
BLUE_SPACE_ship = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png")), 180)
GREEN_SPACE_ship = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png")), 180)
YELLOW_SPACE_ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# lasers
R_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
B_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
G_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
Y_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# ship classes for game
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

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()
    
    
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.velocity = 20
        self.img = img
        
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_ship
        self.laser_img = Y_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health        

    def fire(self, window):
        laser = Laser(self.x, self.y, self.laser_img)        
        self.lasers.append(laser) 
                      
            
    def move_lasers(self):
        for laser in self.lasers:                             
            laser.y -= laser.velocity
                      

        #draw laser moving from ships position upwards (y value gets smaller)
        #include laser velocity

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

# main procedure
def main():
    run = True
    FPS = 60
    level = 0
    lives = 3
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 35)
    player = Player(300, 650)
    enemies = []   
    spawn_count = 5
    velocity = 10  
    enemy_velocity = 2  

    def redraw_window():
        WIN.blit(BG, (0,0))
        for enemy in enemies:
            enemy.draw(WIN)
        player.draw(WIN) 
        for laser in player.lasers:
            laser.draw(WIN)       
        lives_label = main_font.render(f"Lives Remaining : {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level {level}", 1, (255,255,255))
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width()-10,10))        

        pygame.display.update()       


    while run:        
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1            
            for i in range(level*spawn_count):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1000*level, -100*(level/2)), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                run = False
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x + velocity > 0: # left key press
            player.x -= velocity
        if keys[pygame.K_RIGHT] and player.x + velocity + player.get_width() - 20 < WIDTH: # right key press
            player.x += velocity
        if keys[pygame.K_UP] and player.y + velocity > 0: # up key press
            player.y -= velocity
        if keys[pygame.K_DOWN] and player.y + velocity + 95 < HEIGHT: # down key press
            player.y += velocity
        if keys[pygame.K_SPACE]:
            player.fire(WIN)
        
        player.move_lasers()
        for laser in player.lasers:
            if laser.y < -15:
                player.lasers.remove(laser)

        for enemy in enemies:
            enemy.move(enemy_velocity)
            if enemy.y > HEIGHT+100:
                enemies.remove(enemy)

        redraw_window()

main()
