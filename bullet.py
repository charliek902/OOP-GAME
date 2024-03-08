from entity import entity
import pygame
import math
class bullet(entity):
        def __init__(self, state, position_x, position_y, health, type, angle, map):
            self.state = state
            self.position_x = position_x 
            self.position_y = position_y 
            self.health = health
            self.type = type
            self.angle = angle
            self.screen = pygame.display.set_mode((800, 400))
            self.DEFAULT_IMAGE_SIZE = (25, 10)
            self.speed = 5
            self.image = pygame.image.load('game_images/bullet.png')
            self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
            self.image = self.rotate(self.angle)
            self.bullet_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
            self.map = map
        
        def rotate(self, rotation_angle):
             self.image = pygame.transform.rotate(self.image, rotation_angle)
             return self.image
        
        def check_collision_with_entities(self):
            map_entities = self.map.get_entities()
            print(map_entities)

            print('checks collision!')
            
        def update(self):
            self.bullet_rec.x -= self.speed * math.sin(math.radians(self.angle - 90))
            self.bullet_rec.y -= self.speed * math.cos(math.radians(self.angle - 90))
            self.position_x = self.bullet_rec.x
            self.position_y = self.bullet_rec.y
            self.check_collision_with_entities()


            self.screen.blit(self.image, self.bullet_rec)










# do need to ask the question, are the same constructors really necessary for inheriting other attributes + 
# what is the role of super within OOP? what of interfaces? 
