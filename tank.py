# the tank will act like a finite state machine 

from enemy import enemy
from entity import entity
from tankMovement import tankMovement
from bullet import bullet
import math
import pygame
import random
import heapq

class tank(enemy, entity):
    def __init__(self, state, position_x, position_y, health, player, map, type, game):
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
        self.move_strategy = tankMovement(self.map, self.player, self.position_x, self.position_y)
        self.angle = -90
        self.type = type
        self.frame_until_fire = 0
        self.game = game
        self.enemy_bullets = []
    
    def set_hash_name(self, map):
        name = hash(random.randint(0,1000))
        while name in map.entity_hash_names:
            name = hash(random.randint(0,1000))
        return name
    
    def get_angle(self):
        return self.angle
    
    def get_angle_to_player(self):
         # Calculate angle towards the player 
        dx = self.player.position_x - self.position_x
        dy = self.player.position_y - self.position_y
        angle_to_player = math.degrees(math.atan2(dy, dx))

        # Calculate angle difference between current angle and angle to player
        angle_difference = (angle_to_player - self.angle) % 360
        return angle_difference


    def turnToPlayer(self):

        angle_difference = self.get_angle_to_player()
        angle_difference *= -1

        self.image = pygame.image.load('game_images/red_tank.png').convert()
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)

        # Update tank's image with rotated one
        self.image = pygame.transform.rotate(self.image, angle_difference)
 
    def moveToPlayer(self):
        # self.strategy.move(self.x, self.y)
        print('moves to player!')
      #  path = self.move_strategy.move(self.position_x, self.position_y)
      #  self.followPath(path)
        self.turnToPlayer()

        # I think we need to implement a strategy class here
    
    def check_health(self):
        print(self.health)

        if self.health <= 0:
            self.state = 'DEAD'

    def followPath(self, path):
        # should turn to the coordinate on the path 
        # and then move towards it... 

        print('now we need to move to the player...')

    def fire(self):
        distance = self.get_distance_to_player()
        if distance < 15000 and self.frame_until_fire == 0:
            firing_position = self.get_firing_position()
            angle = self.get_angle_to_player()
            player_position = (self.player.position_x, self.player.position_y)
            bullet_created = bullet('alive', firing_position[0], firing_position[1], 100, 'BULLET', angle * -1 + 90, self.map, self.game, 'TANK')
            self.enemy_bullets.append(bullet_created)
            self.frame_until_fire = 20
        elif self.frame_until_fire > 0:
            self.frame_until_fire -= 1


    def update(self):
        self.check_health()
        self.moveToPlayer()
        self.fire()
        self.update_enemy_bullets()
        self.screen.blit(self.image, self.tank_rec)
    
    def get_distance_to_player(self):
        # returns the manhattan distace to the player 
        return ((self.player.position_x - self.position_x) * (self.player.position_x - self.position_x)) \
        + ((self.player.position_y - self.position_y) * (self.player.position_y - self.position_y))


    def get_firing_position(self): 
        firing_position = self.position_x + self.DEFAULT_IMAGE_SIZE[0] / 2 - 5, self.position_y + self.DEFAULT_IMAGE_SIZE[1] / 2
        return firing_position

    def update_enemy_bullets(self):
        for bullet in self.enemy_bullets:
            bullet.update()
