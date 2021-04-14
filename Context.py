import pygame

# I want to import Player here, but then it's circular Player -> Ship -> GameObject -> Context etc
# import Player

class Context:
    def __init__(self, _):
        self.run = True
        self.game_over = False
        self.FPS = 60
        self.level = 0
        self.clock = pygame.time.Clock()
        # font intializer
        pygame.font.init()
        self.main_font = pygame.font.SysFont("comicsans", 35)
        self.player = 0
        self.enemies = []   
        self.lasers = []
        self.powerups = []
        self.spawn_count = 5
        self.enemy_velocity = 2+(.25*self.level)  

    def move_everyone(self):
        for enemy in self.enemies:
            enemy.move(self.enemy_velocity)
        for laser in self.lasers:
            laser.move()
        for powerup in self.powerups:
            powerup.move()
        self.player.move()

    def draw_everyone(self):
        for enemy in self.enemies:
            enemy.draw()
        for laser in self.lasers:
            laser.draw()
        for powerup in self.powerups:
            powerup.draw()
        self.player.draw()

