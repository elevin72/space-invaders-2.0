from GameObject import *
from Player import *
from Enemy import *
from Powerup import *
from Ship import *
from Laser import *

def collide(obj1: GameObject, obj2: GameObject):
    """Collision detection for lasers"""
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    # returns true when there is a collision between the two objects
    return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y))) != None

def do_collision(obj1: GameObject, obj2: GameObject):
    _do_collision(obj1, obj2)
    _do_collision(obj2, obj1)

# This function will do the necessary operations to obj1 based on what obj2 is
def _do_collision(obj1: GameObject, obj2: GameObject):

    # if obj1 is a Player
    if isinstance(obj1, Player):
        if isinstance(obj2, Enemy):
            obj1.health -= 50
        if isinstance(obj2, Powerup):
            obj1.handle_powerup_collision(obj2)
        if isinstance(obj2, Laser) and obj2.color != "yellow":
            obj1.health -= 10

    # if obj1 is an Enemy
    if isinstance(obj1, Enemy): 
        if (
            isinstance(obj2, Laser) and obj2.color == "yellow"
            or isinstance(obj2, Player)
        ):
            # This if statement is required, but whyyyyyy
            if obj1 in ctx.enemies:
                ctx.enemies.remove(obj1)

    # if obj1 is a Laser
    if isinstance(obj1, Laser):
        if (
            (isinstance(obj2, Enemy) and obj1.color == "yellow") or
            (isinstance(obj2, Player) and obj1.color != "yellow")
            ):
            if obj1 in ctx.lasers:
                ctx.lasers.remove(obj1)

    # if obj1 is a Powerup
    if isinstance(obj1, Powerup):
        if isinstance(obj2, Player):
            ctx.powerups.remove(obj1)

