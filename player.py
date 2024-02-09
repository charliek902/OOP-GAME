from entity import entity
from health import health
import pygame
import math


#TODO 
# need to be able to turn left and right and move in that direction using the keys 

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
        self.running = False

        self.bullets = 10
        self.reloading = False

        self.screen = pygame.display.set_mode((800, 400))
        self.speed = speed
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
    
    def move_down(self):
        if self.position_x < 0 and self.angle == 0:
            self.move_down()
            self.shooter_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
            self.shooter_rec.x += self.speed * math.sin(math.radians(self.angle))
            self.shooter_rec.y += self.speed * math.cos(math.radians(self.angle))
            self.position_x = self.shooter_rec.x
            self.position_y = self.shooter_rec.y
            self.running = True


    def move_up(self):
        self.shooter_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
        if self.position_y < 0 and self.angle == 0:
            self.move_down()
        else:
            self.shooter_rec.x -= self.speed * math.sin(math.radians(self.angle))
            self.shooter_rec.y -= self.speed * math.cos(math.radians(self.angle))
            self.position_x = self.shooter_rec.x
            self.position_y = self.shooter_rec.y


 # need to transform the image to a better resolution.... 
    def turn_left(self):
        prev_center = self.shooter_rec.center
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.image = pygame.transform.rotate(self.image, self.rotation_speed)
        self.rect = self.image.get_rect()
        self.rect.center = prev_center
        self.angle += 90
    
    def turn_right(self):
        prev_center = self.shooter_rec.center
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.image = pygame.transform.rotate(self.image, 0 - self.rotation_speed)
        self.rect = self.image.get_rect()
        self.rect.center = prev_center
        self.angle -= 90
    

    def move_Left_UP_diagonal(self):
        self.angle = -45
        prev_center = self.shooter_rec.center
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = prev_center



   # def move_Right_UP_diagonal(self):
                
  #  def move_Right_DOWN_diagonal(self):

   # def move_Left_DOWN_diagonal(self):

        



    def update(self):
        self.check_health()
        self.screen.blit(self.image, self.shooter_rec)


    def fire():
        print('fires!')
        
    def reload():
        print('reloading')
            # would need to initialize a counter and keep it running for the reload 
        
    def initialize_counter():
        print('initializing counter...')
        



        
