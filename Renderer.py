# this class handles page renderering from different changes in state of the Game
import pygame
from text import text

class Renderer():
    def __init__(self, state):
        self.state = state
        self.screen_width = 800
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.test_surface = None
        self.handleStateChange()

    def set_state(self, state):
        self.state = state
    
    def get_state(self):
        return self.state
    
    def handleStateChange(self):
        if self.state == 'HOME':
            return self.handleHomeScreen()
        elif self.state == 'DEATH':
            return self.handleDeath()
        elif self.state == 'PAUSE':
            return self.handlePause()
        elif self.state == 'QUIT':
            return self.handleQuit()


    def handleHomeScreen(self):
        self.render_background()
        resume = text(280, 100, 'Resume / Pause- Click "p"', self.screen)
        controls = text(200, 200, 'Controls- arrow keys to move and space bar to shoot', self.screen)
        quit = text(320, 300, 'Quit- Press escape', self.screen)


    def handleDeath(self):
        self.render_background()
        restart = text(280, 100, 'Restart- Press "r"', self.screen)
        controls = text(200, 200, 'Controls- arrow keys to move and space bar to shoot', self.screen)
        quit = text(320, 300, 'Quit- Press escape', self.screen)
        print(self.state)
    

    def handlePause(self):
        if self.state != 'PAUSE':
            self.state = 'PAUSE'
            self.render_background()
            resume = text(280, 100, 'Resume / Pause- Click "p"', self.screen)
            controls = text(200, 200, 'Controls- arrow keys to move and space bar to shoot', self.screen)
            quit = text(320, 300, 'Quit- Press escape', self.screen)
        else:
            self.state = 'PLAY'

    def render_background(self):
        self.test_surface = pygame.image.load('game_images/background.png')
        self.test_surface = pygame.transform.scale(self.test_surface, (800, 400)).convert_alpha()
        self.screen.blit(self.test_surface, (0,0))
    
    def handleQuit(self):
        pygame.quit()
        exit()




    
    
    
        



