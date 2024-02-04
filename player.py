from entity import entity

class player(entity):
    def __init__(self, state, position_x, position_y):
        self.state = state
        self.position_x = position_x
        self.position_y = position_y
        self.bullets = 10
        self.reloading = False
        # we need to place in an image (probably the rec so that the image can be controlled)

        # we also need to do a movement for the player (left, right, up, down, diagonal in each direction)

        # we also need to do a fire as well 
        
