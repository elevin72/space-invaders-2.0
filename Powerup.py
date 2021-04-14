import time
from GameObject import *
from Player import *

class Powerup(GameObject):

    kinds = {
        "heart" : pygame.image.load(os.path.join("assets", "heart.png")).convert_alpha(),
        "x2" : pygame.image.load(os.path.join("assets", "x2.png")).convert_alpha(),
        "bomb" : pygame.image.load(os.path.join("assets", "bomb.png")).convert_alpha(),
        "explode" : pygame.transform.scale(pygame.image.load(os.path.join("assets", "explode.png")).convert_alpha(), (200,200))
        }

    # note that velocity changed postion in args list
    def __init__(self, x, y, kind, velocity=1):
        super().__init__(x, y, velocity)
        if kind in self.kinds:
            self.kind = kind
            self.img = self.kinds[kind]
        else:
            exit()
            # throw something
            # powerup kind not supported
        self.mask = pygame.mask.from_surface(self.img)

    ## some cool way of externally changing internal behavior of player/other objects
    ## override some method of it for a short period of time, then change back?
    @staticmethod
    async def double_lasers(player: Player):
        # No good, but something like this
        class double_lasers_player(Player):
            def fire(self):
                self.__fire(offset=-8)
                self.__fire(offset=8)
        player_orig = player
        player = double_lasers_player(player.x, player.y, player.velocity)
        time.sleep(5)
        player = player_orig

    def explode(self, img):
        self.velocity = 0
        self.kind = "exploding"
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
