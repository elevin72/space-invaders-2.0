from Powerup import Powerup
import random
import math
import os
from Ship import *
from Laser import *
from Player import Player
from Enemy import Enemy

# font intializer
pygame.font.init()

# Window data
WIDTH, HEIGHT = (750, 750)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders 2.0")

# background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")).convert(), (WIDTH, HEIGHT)) 

RED_SPACE_ship = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png")).convert_alpha(), 180)
BLUE_SPACE_ship = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png")).convert_alpha(), 180)
GREEN_SPACE_ship = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png")).convert_alpha(), 180)
YELLOW_SPACE_ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")).convert_alpha()

R_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png")).convert_alpha()
B_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png")).convert_alpha()
G_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png")).convert_alpha()
Y_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png")).convert_alpha()

HEART_PU = pygame.image.load(os.path.join("assets", "heart.png")).convert_alpha()
X2_PU = pygame.image.load(os.path.join("assets", "x2.png")).convert_alpha()
BOMB_PU = pygame.image.load(os.path.join("assets", "bomb.png")).convert_alpha()

# color dictionary
colors = {
        "red" : (RED_SPACE_ship, R_LASER),
        "blue" : (BLUE_SPACE_ship, B_LASER),
        "green" : (GREEN_SPACE_ship, G_LASER),
        "yellow" : (YELLOW_SPACE_ship, Y_LASER)
        }

powerup_kinds = {
        "heart" : ("heart", HEART_PU),
        "x2" : ("x2", X2_PU),
        "bomb" : ("bomb", BOMB_PU)
        }

def collide(obj1, obj2):
    """Collision detection for lasers"""
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    # returns true when there is a collision between the two objects
    return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y))) != None

def game_over_screen():
    game_over_font = pygame.font.SysFont("comicsans", 50)
    while True:
        WIN.blit(BG, (0, 0))        
        game_over_label1 = game_over_font.render("OH NO! You lost!", 1, (255,255,255))
        game_over_label2 = game_over_font.render("Click the MOUSE to play again.", 1, (255,255,255))
        WIN.blit(game_over_label1, (WIDTH/2 - game_over_label1.get_width()/2, HEIGHT/2 - 75))
        WIN.blit(game_over_label2, (WIDTH/2 - game_over_label2.get_width()/2, HEIGHT/2 + game_over_label1.get_height() + 10 - 75))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
            

def main():
    """Main procedure"""
    run = True
    game_over = False
    FPS = 60
    level = 0
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 35)
    player = Player(300, 650, colors["yellow"], lives=3, health=100)
    enemies = []   
    enemy_lasers = []
    powerups = []
    spawn_count = 5
    velocity = 10  
    enemy_velocity = 2+(.25*level)  

    def redraw_window():
        WIN.blit(BG, (0,0))
        for enemy in enemies:
            enemy.draw(WIN)
        for laser in enemy_lasers:
            laser.draw(WIN);      
        for powerup in powerups:
            powerup.draw(WIN)
        player.draw(WIN) 
        for laser in player.lasers:
            laser.draw(WIN) 
        lives_label = main_font.render(f"Lives Remaining : {player.lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level {level}", 1, (255,255,255))
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width()-10,10))        

        pygame.display.update()       


    while run:        
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1            
            for i in range(level*spawn_count):
                enemy = Enemy(
                        random.randrange(50, WIDTH-100),
                        random.randrange(-1000*level, math.floor(-100*(level/2))),
                        colors[random.choice(["red", "blue", "green"])])
                enemies.append(enemy)
        # while there are still enemies continue generating powerups
        else:
            if random.randint(1,500) == 1:
                powerup = Powerup(
                        random.randrange(50, WIDTH-100),
                        random.randrange(-1000*level, math.floor(-100*(level/2))),
                        powerup_kinds[random.choice(["heart", "x2", "bomb"])])
                powerups.append(powerup)


        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                run = False
        
        if player.health <= 0:            
            player.lives -= 1
            player.health = 100  
            if player.lives == 0:
                game_over = True              
            
            
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
            if player.can_fire():
                player.fire()
            
        for enemy in enemies:
            if random.randrange(1, 250) == level and enemy.y > 0:
                enemy_lasers.append(Laser(enemy.x-(enemy.get_width()*.25), enemy.y, enemy.laser_img, 5 * ((level+5)/5) ))
            if collide(enemy, player):
                player.health -= 50
                enemies.remove(enemy)
                
            enemy.move(enemy_velocity)
            if enemy.y > HEIGHT+50:
                enemies.remove(enemy)
                player.lives -= 1   
                if player.lives == 0:
                    game_over = True 
                
        for laser in enemy_lasers:
            laser.y += laser.velocity
            if laser.y > HEIGHT:
                enemy_lasers.remove(laser)
            if collide(laser, player):
                player.health -= 20
                enemy_lasers.remove(laser)                    

        for powerup in powerups:
            if collide(powerup, player):
                player.handle_powerup(powerup)
                powerups.remove(powerup)
            if powerup.y > HEIGHT:
                powerups.remove(powerup)
            powerup.move()

        player.move_lasers()
        for laser in player.lasers:
            if laser.y < -15:
                # TODO: Sniper Mode. Every laser that misses a ship spawns more ships.
                player.lasers.remove(laser)
            for enemy in enemies:
                if collide(laser, enemy):
                    enemies.remove(enemy)
                    player.lasers.remove(laser)

      
        if game_over:
            game_over_screen()

        redraw_window()

def main_menu():
    menu_font = pygame.font.SysFont("comicsans", 60)
    welcome_label = menu_font.render("Welcome to SPACE INVADERS 2.0!", 1, (142, 123, 225))
    play_label = menu_font.render("Click the MOUSE to play!", 1, (142, 123, 225))
    run = True
    while run:
        WIN.blit(BG, (0,0))  
        WIN.blit(welcome_label, ((WIDTH/2-(welcome_label.get_width()/2)), HEIGHT/2 - 100))    
        WIN.blit(play_label, (WIDTH/2 - play_label.get_width()/2, HEIGHT/2 + welcome_label.get_height()+10 - 100))     
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
                run = False

if __name__ == "__main__":
    main_menu()
