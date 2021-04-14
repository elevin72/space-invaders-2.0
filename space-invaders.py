from Powerup import Powerup
import random
import math
from Context import *
from GameObject import *
from Ship import *
from Laser import *
from Player import *
from Enemy import *
from Util import *

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
    # These 4 variables felt like they didn't belong in ctx. Not sure why
    run = True
    game_over = False
    FPS = 60
    clock = pygame.time.Clock()
    ctx.player = Player(300, 650, 5)

    def redraw_window():
        WIN.blit(BG, (0,0))
        ctx.draw_everyone()
        lives_label = ctx.main_font.render(f"Lives Remaining : {ctx.player.lives}, {ctx.player.health}%", 1, (255,255,255))
        level_label = ctx.main_font.render(f"Level {ctx.level}", 1, (255,255,255))
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width()-10,10))        
        pygame.display.update()       


    while run:        
        clock.tick(FPS)

        # Get player input
        # ctx.player.get_input()
        ctx.move_everyone()

        # Update level
        if len(ctx.enemies) == 0:
            ctx.level += 1            
            for i in range(ctx.level*ctx.spawn_count):
                enemy = Enemy(
                        random.randrange(50, WIDTH-100),
                        random.randrange(-1000*ctx.level, math.floor(-100*(ctx.level/2))),
                        10, # Maybe increase velocity as level increase?
                        random.choice(["red", "blue", "green"]))
                ctx.enemies.append(enemy)
        # while there are still enemies continue generating powerups
        else:
            if random.randint(1,500) == 1:
                powerup = Powerup(
                        random.randrange(50, WIDTH-100),
                        random.randrange(-200, -100),
                        1,
                        random.choice(["heart", "x2", "bomb"]))
                ctx.powerups.append(powerup)

        # check if quit game
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                run = False
        
        # check player health
        if ctx.player.health <= 0:            
            ctx.player.lives -= 1
            ctx.player.health = 100  
            if ctx.player.lives == 0:
                game_over = True              
            
        # enemies shoot
        for enemy in ctx.enemies:
            if random.randrange(1, 250) == ctx.level and enemy.y > 0:
                ctx.lasers.append(Laser(
                    enemy.x-(enemy.get_width()*.25),
                    enemy.y,
                    5 * ((ctx.level+5)/5),
                    enemy.color))

        # calculate collisions
        # inefficient, but cool :)
        for obj1 in ctx.enemies + ctx.lasers + ctx.powerups + [ctx.player]:
            for obj2 in ctx.enemies + ctx.lasers + ctx.powerups + [ctx.player]:
                if collide(obj1, obj2) and obj1 is not obj2:
                    do_collision(obj1, obj2)

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
