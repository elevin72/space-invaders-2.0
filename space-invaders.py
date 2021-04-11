import random
import time
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
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))  

# collision detection for lasers
def collide(obj1, obj2):
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
            
                

# main procedure
def main():
    run = True
    game_over = False
    FPS = 60
    level = 0
    lives = 3
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 35)
    player = Player(300, 650, health=100)
    enemies = []   
    spawn_count = 5
    velocity = 10  
    enemy_velocity = 2+(.25*level)  

    def redraw_window():
        WIN.blit(BG, (0,0))
        for enemy in enemies:
            enemy.draw(WIN)
        player.draw(WIN) 
        for laser in player.lasers:
            laser.draw(WIN) 
        for enemy in enemies:
            for laser in enemy.lasers:
                laser.draw(WIN);      
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
        
        if player.health <= 0:            
            lives -= 1
            player.health = 100  
            if lives == 0:
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
            player.fire(WIN)
            
        for enemy in enemies:
            # probability of an enemy shooting at a given moment is dependent on the level number
            if random.randrange(1, int(250/level)) == level and enemy.y > 0:
                enemy.lasers.append(Laser(enemy.x-(enemy.get_width()*.25), enemy.y, enemy.laser_img, 5+(level*.25)))
            
            if collide(enemy, player):
                player.health -= 50
                enemies.remove(enemy)
                
            enemy.move(enemy_velocity)
            if enemy.y > HEIGHT+50:
                enemies.remove(enemy)
                lives -= 1   
                if lives == 0:
                    game_over = True 
            
            enemy.move_lasers()
            
            for laser in enemy.lasers:
                if laser.y > HEIGHT:
                    enemy.lasers.remove(laser)
                if collide(laser, player):
                    player.health -= 20
                    enemy.lasers.remove(laser)                    

            if game_over:
                game_over_screen()
                
        player.move_lasers()
        
        for laser in player.lasers:
            if laser.y < -15:
                player.lasers.remove(laser)
                
            for enemy in enemies:
                if collide(laser, enemy):
                    enemies.remove(enemy)
                    if laser in player.lasers:
                        player.lasers.remove(laser)
      

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
        
           
main_menu()
