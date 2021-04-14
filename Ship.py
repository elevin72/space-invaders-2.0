from GameObject import *

# Ship could be a useless class, and Enemy and Player could inherit directly from GameObject probably
class Ship(GameObject):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, velocity)  # wait im confused. pass image, but then how does mask work?
            
    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()
        
