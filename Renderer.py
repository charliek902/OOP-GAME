# this class handles page renderering from different changes in state of the Game
import pygame

class Renderer():
    def __init__(self):
        self.state = 'HOME'
        self.screen_height = 800
        self.screen_width = 400
        self.screen = pygame.display.set_mode((self.screen_height, self.screen_width))
        self.handleHomeScreen()

    def set_state(self, state):
        self.state = state
    
    def get_state(self):
        return self.state
    
    def handleStateChange(self):
        if self.state == 'HOME':
            return self.handleHomeScreen(self)
        elif self.state == 'CONTROLS':
            return self.handleControlsDisplay(self)
        elif self.state == 'NEXT LEVEL':
            return self.handleNextLevel(self)
        elif self.state == 'DEATH':
            return self.handleDeath(self)
        elif self.state == 'PAUSE':
            return self.handlePause(self)
        elif self.state == 'QUIT':
            return self.handleQuit(self)


    # controls should be on the home screen 
    def handleHomeScreen(self):
        self.state == 'HOME'
        self.test_surface = pygame.image.load('game_images/background.png')
        self.test_surface = pygame.transform.scale(self.test_surface, (800, 400)).convert_alpha()
        self.screen.blit(self.test_surface, (0,0))


    # this should do a counter on the map with numbers Next level! (3....2....1....)
    def handleNextLevel(self):
        print('next level')

    # render a screen (retry, go to main menu)
    def handleDeath(self):
        print('death')
    
    def handleControlsDisplay(self):
        print('shows a screen with the controls!')



    # buttons need to come here.... (retry, go to main menu, resume, controls)

    def handlePause(self):
        if self.state != 'PAUSE':
            self.state = 'PAUSE'
            self.test_surface = pygame.image.load('game_images/background.png')
            self.test_surface = pygame.transform.scale(self.test_surface, (800, 400)).convert_alpha()
            self.font = pygame.font.SysFont(None, 24)
            self.screen.blit(self.test_surface, (0,0))
            img = self.font.render('Would you like to return back to the game?' , True, "blue")
            self.screen.blit(img, (20, 20))
        else:
            self.state = 'PLAY'
    
    def handleQuit(self):
        pygame.quit()
        exit()




    
    
    
        



