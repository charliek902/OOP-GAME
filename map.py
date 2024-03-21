from entity import entity
import pygame
import heapq
from wall import wall
import random

# this will be a singleton mapping object for all the entities within the game

class map():
    def __init__(self, player):
        self.player = player
        self.entity_hash_names = set()
        self.entity_map = {}
        self.entities = []
        self.enemy_tanks = []
        self.wall_coordinates = []
        self.walls = []
    
    def get_entity(self, name):
        if name in self.entity_map:
            return self.entity_map[name]
        else:
            return None  
    
    def add_entity(self, entity):
        self.entity_map[entity.name] = entity  
        self.entity_hash_names.add(entity.name)
    
    def add_enemy_tank(self, tank):
        self.enemy_tanks.append(tank)
    
    
    def get_enemy_tanks(self):
        return self.enemy_tanks

    def remove_entity(self, entity):
        if entity.name:
            del self.entity_map[entity.name]
            self.entity_hash_names.remove(entity.name)
    
    def get_player(self):
        return self.player
    
    def get_entities(self):
        return self.entity_map
    
    def remove_enemy_tank(self, tank):
        self.enemy_tanks.remove(tank)

    # basically just need to increase x by 25 and y by 25 
    def get_wall_locations(self):
        return self.wall_coordinates

    # want to generate 12 walls for the game which are roughly spaced out 
    def generate_walls(self):
        # this boolean will be set to true if another wall is within the random coordinates range of 25 
        start_x = 0
        end_x = 50
        start_y = 50
        end_y = 100

        for i in range(0, 12):
            x = random.randint(start_x, end_x)
            y = random.randint(start_y, end_y)
            self.wall_coordinates.append([x, y])
            game_wall = wall('alive', x, y, 100, 'WALL')
            self.walls.append(game_wall)
            # resets the x value back to 0 when walls have been created at the end of the x axis of the map 
            if start_x > 700:
                start_y += 150
                end_y += 150
                start_x = -200
                end_x = 0
            start_x += 300
            end_x += 300

    
    def update_walls(self):
        for wall in self.walls:
            wall.update()

    
    

