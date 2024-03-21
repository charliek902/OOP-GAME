from entity import entity
import pygame

class healthbar(entity):
    def __init__(self, x_position, y_position, width, height, points, screen, player):

        self.width = width
        self.height = height
        self.points = points
        self.screen = screen
        self.player = player
        self.screen = pygame.display.set_mode((800, 400))
        self.type = None

    def display(self):
        self.ratio = self.player.health / 100
        pygame.draw.rect(self.screen, "red", (self.player.position_x - 15, self.player.position_y - 20, self.width, self.height))
        pygame.draw.rect(self.screen, "green", (self.player.position_x - 15, self.player.position_y - 20, self.width * self.ratio, self.height))
        pygame.display.flip() 
        
    def update(self):
        self.display()
    



        
        


    