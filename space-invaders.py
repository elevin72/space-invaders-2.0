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

# main procedure
def main():
    run = True
    FPS = 60
    level = 0
    lives = 3
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 35)
    player = Player(300, 650, health=100)
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
        
        if player.health == 0:
            break
            
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
            # probability of an enemy shooting at a given moment is 1 in 250
            if random.randrange(1, 250) == level and enemy.y > 0:
                enemy.lasers.append(Laser(enemy.x-(enemy.get_width()*.25), enemy.y, enemy.laser_img, 5))
            
            if collide(enemy, player):
                player.health -= 50
                enemies.remove(enemy)
                
            enemy.move(enemy_velocity)
            if enemy.y > HEIGHT+100:
                enemies.remove(enemy)    
            
            enemy.move_lasers()
            
            for laser in enemy.lasers:
                if laser.y > HEIGHT:
                    enemy.lasers.remove(laser)
                if collide(laser, player):
                    player.health -= 20
                    enemy.lasers.remove(laser)                    
        
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

main()
