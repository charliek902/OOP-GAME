from entity import entity
from health import health
from bullet import bullet
import pygame
import math


#TODO
# find natural position of the gun on the player depending on the top left and the angle of the player

class player(entity):
    def __init__(self, state, position_x, position_y, speed, angle, rotation_speed, points, map):
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.position_y = position_y
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
        self.move_player()


    def move_up(self):
        self.turn(-270)
        self.check_can_move()
        self.move_player()
    
    def move_right(self):
        self.turn(0)
        self.move_player()

    def move_left(self):
        self.turn(-180)
        self.move_player()


    def moveDiagonalUpRight(self):
        self.turn(45)
        self.move_player()

    def moveDiagonalUpLeft(self):
        self.turn(-225)
        self.move_player()


    def moveDiagonalDownLeft(self):
        self.turn(-135)
        self.move_player(True)


    def moveDiagonalDownRight(self):
        self.turn(-45)
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
        # could update player point score here... 
        self.screen.blit(self.image, self.shooter_rec)
    
    def update_player_bullets(self):
        for bullet_instance in self.bullets:
            if isinstance(bullet_instance, bullet):
                bullet_instance.update()

    def fire(self):
        firing_position = self.get_firing_position()
        print(firing_position)

        if firing_position:
            bullet_created = bullet('alive', firing_position[0], firing_position[1], 100, 'BULLET', self.angle, self.map)
            self.bullets.append(bullet_created)
            print('fires!')
        else:
            print('unsuccesful!')

    def check_can_move(self):
        possible_x_position = self.shooter_rec.x - self.speed * math.sin(math.radians(self.angle - 90))
        possible_y_position = self.shooter_rec.y - self.speed * math.cos(math.radians(self.angle - 90))
        map_entities = self.map.get_entities()
        # need to check map_entities if their radius intersects with the player...


# we need to get the firing position and this is based off the angle 
    def get_firing_position(self): 
        firing_position = 0, 0
        if self.angle == 0:
            firing_position = self.position_x + self.DEFAULT_IMAGE_SIZE[0], self.position_y + 0.8 * (self.DEFAULT_IMAGE_SIZE[1])
            return firing_position
        elif self.angle == -90:
            firing_position = self.position_x + 0.2 * self.DEFAULT_IMAGE_SIZE[0], self.position_y + (self.DEFAULT_IMAGE_SIZE[1])
            return firing_position
        elif self.angle == -180:
            firing_position = self.position_x - self.DEFAULT_IMAGE_SIZE[0] * 0.8, self.position_y + (self.DEFAULT_IMAGE_SIZE[1] * 0.2)
            return firing_position
        
        elif self.angle == -270:
            firing_position = self.position_x + (self.DEFAULT_IMAGE_SIZE[0] * 0.7), self.position_y - (self.DEFAULT_IMAGE_SIZE[1] * 0.8)
            return firing_position
        
        return None


    def reload():
        print('reloading')
            # would need to initialize a counter and keep it running for the reload 
        
    def initialize_counter():
        print('initializing counter...')
        



        
