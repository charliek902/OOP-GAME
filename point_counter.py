from entity import entity
class point_counter(entity):
    def __init__(self, x, y, initial_points):
        self.x = x
        self.y = y
        self.figure = initial_points
        
        # need to draw the point cointer in a certain place... 

        # walls, enemies and users should not spawn there... 
    
    def update(self, figure):
        self.figure = figure


        