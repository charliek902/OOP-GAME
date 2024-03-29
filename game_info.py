from entity import entity
import pygame

# in this class the player points, the number of rounds completed and the number of remaining enemies left is rendered on the screen 

class game_info(entity):
    def __init__(self, x, y, renderer):
        self.x = x
        self.y = y
        self.renderer_state = renderer.state
        self.screen = pygame.display.set_mode((800, 400))
        self.font = pygame.font.SysFont(None, 24)


    def update(self, rounds_completed, remaining_enemies):
        img = self.font.render('Rounds completed: ' + str(rounds_completed - 1), True, "blue")
        self.screen.blit(img, (220, 20))
        img = self.font.render(' Enemies remaining: ' + str(remaining_enemies), True, "blue")
        self.screen.blit(img, (520, 20))





