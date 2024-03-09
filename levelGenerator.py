from tankFactory import tankFactory 
from map import map 

class levelGenerator():
    def __init__(self, map, player):
        self.level = 1
        self.player = player
        self.map = map
        self.enemy_tank_factory = tankFactory(self.map, self.player)
        self.enemy_tanks = []
        self.remaining_enemy_tanks = 0
        self.rendering = False
        # creating enemy tank factory on constructor... 
        self.enemy_tank_factory.create_enemy_tanks()


    # class tank(enemy, entity):
    # def __init__(self, state, position_x, position_y, health, player, map, type):

    def level_up(self):
        self.level += 1
        self.render_level_up()
        self.rendering = False
        self.enemy_tank_factory.create_enemy_tanks()
    
    def render_level_up(self):
        self.rendering = True
        print('levelling up appear on the screen')
    
    def update(self):
        if len(self.map.get_enemy_tanks()) == 0:
            self.level_up()
        else:
            enemies = self.enemy_tank_factory.get_enemies()
            self.remaining_enemy_tanks = len(enemies)
            for enemy in enemies:
                if enemy.state != 'DEAD':
                    enemy.update()
                else:
                    self.enemy_tank_factory.remove_tank(enemy)
                    self.map.remove_enemy_tank(enemy)







    



