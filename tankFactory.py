from tank import tank
from map import map
import random 
from healthbar import healthbar
import pygame

class tankFactory():
    def __init__(self, map, player, game):
        self.level = 1
        self.enemies = 0
        self.health = 20
        # 16 will be the maximum amount of enemy tanks that will face the user in a single round... 
        self.maximum_tanks = 17
        self.map = map
        self.player = player
        self.enemies_list = []
        self.enemy_starting_coordinates = []
        self.game = game
    
    # we need to create L, R, Up and Down tanks of the screen... 
    def generate_random_coordinates(self):
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        while (x, y) in self.enemy_starting_coordinates:
            x = random.randint(0, 400)
            y = random.randint(0, 400)
        self.enemy_starting_coordinates.append([x, y])
        return x, y


    def create_enemy_tanks(self):
        if self.enemies < self.maximum_tanks and self.enemies != 0:
            self.enemies *= 2
        elif self.enemies == 0:
            self.enemies = 1
        if self.health < 100:
            self.health += 10
        
        # need to put enemy tanks in different locations... (really important now)
            
        for i in range(0, self.enemies):
            x, y = self.generate_random_coordinates()
            enemy_tank = tank('SEARCH', x, y, self.health, self.player, self.map, 'TANK', self.game)
            self.test_surface = pygame.image.load('game_images/background.png')
            self.test_surface = pygame.transform.scale(self.test_surface, (800, 400)).convert_alpha()
            # 60 ,10, 100, game_state.test_surface, shooter
            self.map.add_entity(enemy_tank)
            self.map.add_enemy_tank(enemy_tank)
            self.enemies_list.append(enemy_tank)
    
    def get_enemies(self):
        return self.enemies_list

    def remove_tank(self, tank):
        self.enemies_list.remove(tank)
    
    

    
