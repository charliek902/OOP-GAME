from entity import entity

class wall(entity):
    def __init__(self, state, x_position, y_position, health):
        self.state = state
        self.x_position = x_position
        self.y_position = y_position
        self.health = health
    
    def update():
        print('updates!')

