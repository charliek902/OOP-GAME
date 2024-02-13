from entity import entity
import pygame


#700, 10, 60, 20, 100, game_state.test_surface, shooter.health)

class healthbar(entity):
    def __init__(self, x_position, y_position, width, height, points, screen, player):

        self.position_x = x_position
        self.position_y = y_position
        self.width = width
        self.height = height
        self.points = points
        self.screen = screen
        self.player = player

    def display(self):
        print(self.player)
        self.ratio = self.player.get_health() / self.points
        pygame.draw.rect(self.screen, "red", (self.position_x, self.position_y, self.width, self.height))
        pygame.draw.rect(self.screen, "green", (self.position_x, self.position_y, self.width * self.ratio, self.height))

    
    def update(self):
        self.display()

        
        


    