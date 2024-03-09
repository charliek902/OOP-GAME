from entity import entity
import pygame


# we need the round and we need the remaining enemies 

class point_counter(entity):
    def __init__(self, x, y, initial_points):
        self.x = x
        self.y = y
        self.figure = initial_points
        self.screen = pygame.display.set_mode((800, 400))
        self.font = pygame.font.SysFont(None, 24)
        img = self.font.render('Points:' + str(self.figure) + ' Rounds completed: ' + str(0) + ' Rounds remaining: ' + str(0), True, "blue")
        self.screen.blit(img, (20, 20))
        
        # need to draw the point cointer in a certain place... 

        # walls, enemies and users should not spawn there... 
    
    def update(self, player_points, rounds_completed, remaining_enemies):
        self.figure = player_points
        img = self.font.render('Points: ' + str(self.figure), True, "blue")
        self.screen.blit(img, (20, 20))
        img = self.font.render('Rounds completed: ' + str(rounds_completed), True, "blue")
        self.screen.blit(img, (220, 20))
        img = self.font.render(' Rounds remaining: ' + str(remaining_enemies), True, "blue")
        self.screen.blit(img, (520, 20))





