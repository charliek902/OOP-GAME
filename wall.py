from entity import entity
import pygame

class wall(entity):
    def __init__(self, state, position_x, position_y, health, type):
        self.state = state
        self.position_x = position_x
        self.position_y = position_y
        self.health = health
        self.type = type
        self.DEFAULT_IMAGE_SIZE = (40, 40)
        self.image = pygame.image.load('game_images/wall.png')
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.wall_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
        self.screen = pygame.display.set_mode((800, 400))
    
    def update(self):
        self.screen.blit(self.image, self.wall_rec)

