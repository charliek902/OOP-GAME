from entity import entity
from health import health
from bullet import bullet
import pygame
import random
import math


#TODO
# find natural position of the gun on the player depending on the top left and the angle of the player

class player(entity):
    def __init__(self, state, position_x, position_y, speed, angle, rotation_speed, points, map, game):
        self.position_x = position_x
        self.position_y = position_y
        self.name = hash(random.randint(0, 10000))
        self.game = game
        self.bullets = []
        self.DEFAULT_IMAGE_SIZE = (25, 25)
        self.image = pygame.image.load('game_images/shooter.png')
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.shooter_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
        self.state = state
        player_health = health(100)
        self.health = player_health.get_health()
        self.points = points
        self.map = map
        self.reloading = False
        self.screen = pygame.display.set_mode((800, 400))
        self.speed = 3
        self.angle = angle
        self.rotation_speed = rotation_speed
        self.frames_until_player_can_fire = 0

    def check_health(self):

        if self.health <= 0:
            self.state = 'DEATH'
            if self.state == 'DEATH':
                pygame.quit()
                exit()

    def get_position(self):
        return self.position_x, self.position_y

    def get_angle(self):
        return self.angle
    
    def move_down(self):
        self.turn(-90)
        if self.check_can_move() and self.check_valid_player_bounds():
            self.move_player()


    def move_up(self):
        self.turn(-270)
        if self.check_can_move() and self.check_valid_player_bounds():
            self.move_player()
    
    def move_right(self):
        self.turn(0)
        if self.check_can_move() and self.check_valid_player_bounds():
            self.move_player()

    def move_left(self):
        self.turn(-180)
        if self.check_can_move() and self.check_valid_player_bounds():
            self.move_player()


    def moveDiagonalUpRight(self):
        self.turn(45)
        if self.check_can_move() and self.check_valid_player_bounds():
            self.move_player(True)

    def moveDiagonalUpLeft(self):
        self.turn(-225)
        if self.check_can_move() and self.check_valid_player_bounds():
            self.move_player(True)


    def moveDiagonalDownLeft(self):
        self.turn(-135)
        if self.check_can_move() and self.check_valid_player_bounds():
            self.move_player(True)


    def moveDiagonalDownRight(self):
        self.turn(-45)
        if self.check_can_move() and self.check_valid_player_bounds():
            self.move_player(True)
 
    
    def move_player(self, increaseSpeed=False):
        # this was built in due to noticeable differences in speeds between diagonals
        if increaseSpeed:
            self.shooter_rec.x -= (self.speed + 0.7) * math.sin(math.radians(self.angle - 90))
            self.shooter_rec.y -= (self.speed + 0.7) * math.cos(math.radians(self.angle - 90))
            self.position_x = self.shooter_rec.x
            self.position_y = self.shooter_rec.y
        else:
            self.shooter_rec.x -= self.speed * math.sin(math.radians(self.angle - 90))
            self.shooter_rec.y -= self.speed * math.cos(math.radians(self.angle - 90))
            self.position_x = self.shooter_rec.x
            self.position_y = self.shooter_rec.y
    
    def set_map(self, map):
        self.map = map


 # need to transform the image to a better resolution.... 
    def turn(self, angle):
        self.image = pygame.image.load('game_images/shooter.png').convert()
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.angle = angle
        
        
    def get_health(self):
        return self.health

    def update(self):
        self.check_health()
        # this frames_until_player_can_fire for the update ensures that the user cannot continiously fire
        if self.frames_until_player_can_fire > 0:
            self.frames_until_player_can_fire -= 1

        # could update player point score here... 
        self.screen.blit(self.image, self.shooter_rec)
    
    def update_player_bullets(self):
        for bullet_instance in self.bullets:
            if isinstance(bullet_instance, bullet):
                bullet_instance.update()
    
    def update_points(self):
        return self.points

    def fire(self):
        if self.frames_until_player_can_fire == 0:
            firing_position = self.get_firing_position()
            bullet_created = bullet('alive', firing_position[0], firing_position[1], 100, 'BULLET', self.angle, self.map, self.game)
            self.bullets.append(bullet_created)
            self.frames_until_player_can_fire = 30

            print('below are the points count...')
            print(self.game.points)


# this function also needs to check the angle of the player as well, 

    def check_can_move(self):
        possible_x_position = self.shooter_rec.x - self.speed * math.sin(math.radians(self.angle - 90))
        possible_y_position = self.shooter_rec.y - self.speed * math.cos(math.radians(self.angle - 90))
        # checks the wall locations and whether the player can move there 
        wall_locations = self.map.get_wall_locations()
        for dx, dy in wall_locations:
            if self.angle == 0 or self.angle == -270:
                if (dx - 25 <= possible_x_position <= dx + 40) and (dy - 25 <= possible_y_position <= dy + 40):
                    return False
            elif (dx <= possible_x_position <= dx + 40) and (dy <= possible_y_position <= dy + 40):
                return False
        return True

     #   map_entities = self.map.get_entities()

# we need to get the firing position and this is based off the angle 
    def get_firing_position(self): 
        firing_position = 0, 0
        if self.angle == 0:
            firing_position = self.position_x + self.DEFAULT_IMAGE_SIZE[0], self.position_y + 0.6 * (self.DEFAULT_IMAGE_SIZE[1])
            return firing_position
        elif self.angle == -45:
            firing_position = self.position_x  + self.DEFAULT_IMAGE_SIZE[0] * 0.8, self.position_y + (self.DEFAULT_IMAGE_SIZE[1] * 1.2)
            return firing_position
        elif self.angle == -90:
            firing_position = self.position_x + 0.1 * self.DEFAULT_IMAGE_SIZE[0], self.position_y + (self.DEFAULT_IMAGE_SIZE[1])
            return firing_position
        elif self.angle == -135:
            firing_position = self.position_x - self.DEFAULT_IMAGE_SIZE[0], self.position_y + (self.DEFAULT_IMAGE_SIZE[1])
            return firing_position
        elif self.angle == -180:
            firing_position = self.position_x - self.DEFAULT_IMAGE_SIZE[0] * 0.8, self.position_y + (self.DEFAULT_IMAGE_SIZE[1] * 0.1)
            return firing_position
        elif self.angle == -225:
                firing_position = self.position_x - self.DEFAULT_IMAGE_SIZE[0] * 0.1, self.position_y - (self.DEFAULT_IMAGE_SIZE[1] * 0.6)
                return firing_position
        elif self.angle == -270:
            firing_position = self.position_x + (self.DEFAULT_IMAGE_SIZE[0] * 0.6), self.position_y - (self.DEFAULT_IMAGE_SIZE[1] * 0.8)
            return firing_position
        elif self.angle == 45:
            firing_position = self.position_x + (self.DEFAULT_IMAGE_SIZE[0] * 0.9), self.position_y - (self.DEFAULT_IMAGE_SIZE[1] * 0.1)
            return firing_position
        else:
            return None
    
    def check_valid_player_bounds(self):
        if self.position_y <= 0 and (self.angle == -225 or self.angle == 45 or self.angle == -270):
            return False
        elif self.position_x <= 0 and (self.angle == -135 or self.angle == -225 or self.angle == -180):
            return False
        elif self.position_y >= 375 and (self.angle == -135 or self.angle == -45 or self.angle == -90):
            return False
        elif self.position_x >= 775 and (self.angle == -45 or self.angle == 45 or self.angle == 0):
            return False
        return True
        
        
    def reload():
        print('reloading')
            # would need to initialize a counter and keep it running for the reload 
        
    def initialize_counter():
        print('initializing counter...')
        



        
