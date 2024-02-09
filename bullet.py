from entity import entity
class bullet(entity):
        def __init__(self, state, position_x, position_y, health):
            self.state = state
            self.position_x = position_x
            self.position_y = position_y
            self.health = health



# do need to ask the question, are the same constructors really necessary for inheriting other attributes + 
# what is the role of super within OOP? what of interfaces? 
