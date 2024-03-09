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
        self.entity_map[entity.name] = entity  # Store the entire entity object
        self.entity_hash_names.add(entity.name)
    
    def add_enemy_tank(self, tank):
        self.enemy_tanks.append(tank)
    
    def del_enemy_tank(self, tank):
        self.enemy_tanks.remove(tank)
    
    def get_enemy_tanks(self):
        return self.enemy_tanks

    def remove_entity(self, entity):
        if entity.name:
            del self.entity_map[entity.name]
            self.entity_hash_names.remove(entity.name)
    
    def convert_entity_map_to_array(self):
        self.entities = list(self.entity_map)

    def update_entity_location(self, object_name, x_position, y_position):
        self.entity_map[object_name] = [x_position, y_position]

    def get_user_radius_border(self):
        # LEFT, RIGHT, UP, DOWN
        return [self.player.x - 100, self.player.x + 100, self.player.y - 100, self.player.y + 100]

    # here we want to filter the map for the entities which are closest to the object (I say within 50 pixels)
    def get_nearby_entities_on_trajectory(self, object):
        entities_to_dodge = []
        heapq.heapify(entities_to_dodge)
        self.convert_entity_map_to_array()
        # here we need to filter the entities and get entities and their types within the radius of the entitiy in question
        nearby_entities = self.entities.filter(self.retrieve_entities(object), self.entities)
        for entity in nearby_entities:
            if entity.type == 'BULLET' or entity.type == 'TANK':
                distance = 0
                # need to calculate the distance between the player and the entity and also need to 
                # calculate the trajectory of the entity and whether it will hit the tank 
                
                heapq.heappush(entities_to_dodge, (distance, entity))

        return entities_to_dodge

    def get_entities(self):
        return self.entity_map
    
    def remove_enemy_tank(self, tank):
        self.enemy_tanks.remove(tank)


    def retrieve_entities(self, object):
        lower_x_bound = object.x_position - 50
        upper_x_bound = object.x_position + 50
        lower_y_bound = object.y_position - 50
        upper_y_bound = object.y_position + 50
        if self.entities.x_position > lower_x_bound and self.entities.x_position < upper_x_bound \
         and self.entities.y_position < upper_y_bound and self.entities.y_position > lower_y_bound:
            return True
        return False
    
    # basically just need to increase x by 25 and y by 25 
    def get_wall_locations(self):
        return self.wall_coordinates

    
    # want to generate 8 walls for the game
    def generate_walls(self):
        # this boolean will be set to true if another wall is within the random coordinates range of 25 
        in_range = True
        repeat = False
        for i in range(0, 8):
            x = random.randint(100, 775)
            y = random.randint(50, 375)
            while (x, y) in self.wall_coordinates or in_range:
                x = random.randint(50, 400)
                y = random.randint(50, 400)

                for dx, dy in self.wall_coordinates:
                    if (x <= dx + 25 or x >= dx - 25) and (y <= dy + 25 or y >= dy - 25):
                        in_range = True
                        repeat = False
                
                if repeat == False:
                    in_range = False


            self.wall_coordinates.append([x, y])
            game_wall = wall('alive', x, y, 100, 'WALL')
            self.walls.append(game_wall)
    
    def update_walls(self):
        for wall in self.walls:
            wall.update()

    
    

