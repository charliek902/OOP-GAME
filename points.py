from entity import entity
class points(entity):
    def __init__(self, state, position_x, position_y, health):
        self.state = state
        self.position_x = position_x
        self.position_y = position_y
        self.health = health

    