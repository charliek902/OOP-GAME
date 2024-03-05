from entity import entity
import pygame

# this will be a singleton mapping object for all the entities within the game

class map():
    def __init__(self, player):
        self.player = player
        self.entity_hash_names = []
        self.entity_map = {}
        self.entities = []
    
    def get_entity(self, name):
        return self.entity_map[name]
    
    def add_entity(self, entity):
        if entity.name:
            self.entity_map[entity.name] = [entity.position_x, entity.position_y]
            self.entity_hash_names.append(entity.name)

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
    def get_nearby_entities(self, object):
        self.convert_entity_map_to_array()
        # here we need to filter the entities and get entities and their types within the radius of the entitiy in question
        nearby_entities = self.entities.filter(self.retrieve_entities(object), self.entities)
        return nearby_entities
    
    def retrieve_entities(self, object):
        lower_x_bound = object.x_position - 50
        upper_x_bound = object.x_position + 50
        lower_y_bound = object.y_position - 50
        upper_y_bound = object.y_position + 50
        if self.entities.x_position > lower_x_bound and self.entities.x_position < upper_x_bound \
         and self.entities.y_position < upper_y_bound and self.entities.y_position > lower_y_bound:
            return True
        return False
    
    # we need to check this map for nearby entities (tanks will use this and so will the user)
    

