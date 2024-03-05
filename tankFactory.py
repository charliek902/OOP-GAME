from tank import tank
from map import map

class tankFactory():
    def __init__(self, map, player):
        self.level = 1
        self.enemies = 2
        self.health = 20
        self.maximum_tanks = 33
        self.map = map
        self.player = player
    
    def create_enemy_tanks(self):
        if self.enemies < self.maximum_tanks:
            self.enemies *= 2
        if self.health < 100:
            self.health += 10
        
        # need to put enemy tanks in different locations... 
        
        for i in range(0, self.enemies + 1):
            enemy_tank = tank('SEARCH', 150, 150, 100, self.player, self.map, 'TANK')
            self.map.add_entity(enemy_tank)
            self.map.add_enemy_tank(enemy_tank)

            #   def __init__(self, state, position_x, position_y, health, player, map, type):

    
