from Laser import *

class Powerup(Laser):
    def __init__(self, x, y, kind, velocity=1):
        self.x = x
        self.y = y
        self.velocity = velocity
        if kind[0] in {"heart", "bomb", "x2"}:
            self.kind = kind[0]
        else:
            exit()
            # throw something
            # powerup type not supported
        self.img = kind[1]
        self.mask = pygame.mask.from_surface(self.img)

    # anti-pattern much??
    def move(self):
        self.y += self.velocity

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
