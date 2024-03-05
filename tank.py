# the tank will act like a finite state machine 

from enemy import enemy
from entity import entity
from tankMovement import tankMovement
import pygame
import random



# needs to turn move towards the player
# needs to calculate the quickest path to the distance from the player (through a dfs) ----> strategy here???
# so needs to go to the outer rim of player radius, for each iteration needs to calculate path to player
# within this path tank should rotate and go to each coordinate of the path which has been constructed via a dfs

# dfs itself would prioritise directions to be closer to the player for each iteration of the dfs 


# we would have a path (array of coordinates) ---> this would constanly be appended to 


# within range the tanks need to turn towards the player 

# for other tanks their behavior will be different 

# defualt state of the tank is down 




# different kinds of STATES for the tank:

# DODGE STATE 
# SEARCH STATE
# FIRE STATE 


class tank(enemy, entity):
    def __init__(self, state, position_x, position_y, health, player, map):
        self.state = state
        self.entity_hash_name = hash(random.randint(0, 1000))
        self.position_x = position_x
        self.position_y = position_y
        self.health = health
        self.player = player
        self.screen = pygame.display.set_mode((800, 400))
        self.DEFAULT_IMAGE_SIZE = (25, 25)
        self.image = pygame.image.load('game_images/red_tank.png')
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.tank_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
        self.name = self.set_hash_name(map)
        self.map = map
        self.move_strategy = tankMovement(self.map)
    

    def interpret_state(self):
        # should first check if state should be DODGE
        entities_nearby = self.map.get_nearby_entities()
        # if one is a bullet --> set state to Dodge
        self.state = 'DODGE'
        # dodge the closest bullet 
        self.dodge_entity()

        # if the enemy is within firing distance, enemy should fire
        user_radius = self.map.get_user_radius_border()

        self.state == 'FIRE'
        # if current tank within this radius, fire! 
        self.fire()

        # else state should be in search Mode 

        # 2 different types of search Mode --> check if you can go straight to the player 
        # check if path is clear 
        # else you need to follow the dfs path 
        # this path would have to be constructed each time (maybe the strategy class would have to do this....)

    
    def check_radius(self):
        print('checks radius')
        # maybe this should check coordinates of the singleton map object
    
    def set_hash_name(self, map):
        name = hash(random.randint(0,1000))
        while name in map.entity_hash_names:
            name = hash(random.randint(0,1000))
        return name

    def turnToPlayer():
        print('turns to the player')
 
    def move(self):
        print('moves to player!')
        path = self.move_strategy.generate_path()
        self.move_to_player(path)

        # I think we need to implement a strategy class here
    

    def move_to_player(self, path):
        print('now we need to move to the player...')

    
 

        

    
    def fire():
        print('attacks!')
        # NB: this should be firing when at a certain distance 

    def update(self):
        self.move()
        self.check_collide()
        self.map.update_entity_location(self.name, self.position_x, self.position_y)
        self.screen.blit(self.image, self.tank_rec)
    
    def dodge_entity(self, entities):
        print('dodging action to be done here!')
