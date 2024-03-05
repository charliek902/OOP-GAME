from tank import tank
from map import map

class tankFactory():
    def __init__(self, map):
        self.level = 1
        self.enemies = 2
        self.health = 20
        self.maximum_tanks = 33
        self.map = map
    
    def create_enemy_tanks(self, level):
        if self.enemies < self.maximum_tanks:
            self.enemies *= 2
        if self.health < 100:
            self.health += 10
        
        # now we want to do a loop and construct an object within that loop 
        

        





     ##   self.map.add_entity(tank)
      #  self.map.add_enemy_tank(tank)


        


        print('creates a tank!')
