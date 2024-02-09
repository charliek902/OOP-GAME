import pygame

class game():
    def __init__(self, renderer, state, screen_height, screen_width):
        self.renderer = renderer
        self.state = state
        self.screen = pygame.display.set_mode((screen_height, screen_width))
        self.test_surface = pygame.image.load('game_images/background.png')
        self.test_surface = pygame.transform.scale(self.test_surface, (800, 400)).convert_alpha()


    def play(self):
        print('plays the game!')
    
    def update(self):
        self.screen.blit(self.test_surface, (0,0))
