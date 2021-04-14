from Ship import *
from Laser import *
from timeit import default_timer as timer

class Player(Ship):
    def __init__(self, x, y, velocity, lives=3, health=100):
        super().__init__(x, y, velocity)
        self.lives = lives
        self.health = health   
        self.cool_down_timer = 0
        self.x2_timer = 0
        self.img = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")).convert_alpha()
        self.mask = pygame.mask.from_surface(self.img)

    def move(self):
        self.get_input()

    def draw(self):
        WIN.blit(self.img, (self.x, self.y))

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x + self.velocity > 0: # left key press
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x + self.velocity + self.get_width() - 20 < WIDTH: # right key press
            self.x += self.velocity
        if keys[pygame.K_UP] and self.y + self.velocity > 0: # up key press
            self.y -= self.velocity
        if keys[pygame.K_DOWN] and self.y + self.velocity + 95 < HEIGHT: # down key press
            self.y += self.velocity
        if keys[pygame.K_SPACE]:
            if self.can_fire():
                self.fire()

    def __fire(self, offset=0):
        ctx.lasers.append(Laser(self.x + offset, self.y, -10, "yellow"))

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



