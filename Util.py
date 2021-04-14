from GameObject import GameObject

def collide(obj1: GameObject, obj2: GameObject):
    """Collision detection for lasers"""
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    # returns true when there is a collision between the two objects
    return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y))) != None

