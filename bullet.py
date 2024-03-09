from entity import entity
import pygame
import math
class bullet(entity):
        def __init__(self, state, position_x, position_y, health, type, angle, map, game):
            self.state = state
            self.position_x = position_x 
            self.position_y = position_y 
            self.game = game
            self.points = game.points
            self.health = health
            self.type = type
            self.angle = angle
            self.screen = pygame.display.set_mode((800, 400))
            self.DEFAULT_IMAGE_SIZE = (25, 10)
            self.speed = 7
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

            for entity_name, entity_positions in map_entities.items():
                entity_x = entity_positions[0]  
                entity_y = entity_positions[1]  
                entity_width = 25  
                entity_height = 25  

                if (entity_x <= self.position_x <= entity_x + entity_width) and \
                (entity_y <= self.position_y <= entity_y + entity_height):
                    entity_damaged = self.map.get_entity(entity_name)
                    self.points += 10
                    print(entity_damaged)

                    # need to remove the health by 10 from the enemy tank and you also need to remove the bullet 
                    # from the game 


                   # entity_damaged.health -= 10
  
            
        def update(self):
            self.bullet_rec.x -= self.speed * math.sin(math.radians(self.angle - 90))
            self.bullet_rec.y -= self.speed * math.cos(math.radians(self.angle - 90))
            self.position_x = self.bullet_rec.x
            self.position_y = self.bullet_rec.y
            self.check_collision_with_entities()
            self.game.points = self.points
            self.screen.blit(self.image, self.bullet_rec)


