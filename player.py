from entity import entity
from health import health
import pygame
import math


#TODO
# find natural position of the gun on the player depending on the top left and the angle of the player

class player(entity):
    def __init__(self, state, position_x, position_y, speed, angle, rotation_speed, points):
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.position_y = position_y
        self.DEFAULT_IMAGE_SIZE = (25, 25)
        self.image = pygame.image.load('game_images/shooter.png')
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.shooter_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
        self.state = state
        player_health = health(100)
        self.health = player_health.get_health()
        self.points = points

        self.bullets = 10
        self.reloading = False

        self.screen = pygame.display.set_mode((800, 400))
        self.speed = 3
        self.angle = angle
        self.rotation_speed = rotation_speed

    def check_health(self):

        if self.health <= 0:
            print('fuck off')
            '''
            self.state = 'DEATH'
            if self.state == 'DEATH':
                pygame.quit()
                exit()
            '''


    def get_position(self):
        return self.position_x, self.position_y

    def get_angle(self):
        return self.angle
    
    
    def move_down(self):
        self.turn(-90)
        self.move_player()


    def move_up(self):
        self.turn(-270)
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


    def fire(self):
        print(self.angle)
        print('fire')
        print('fires!')
        
    def reload():
        print('reloading')
            # would need to initialize a counter and keep it running for the reload 
        
    def initialize_counter():
        print('initializing counter...')
        



        
