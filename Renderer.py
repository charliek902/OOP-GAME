# this class handles page renderering from different changes in state of the Game
import pygame

class Renderer():
    def __init__(self):
        self.state = 'LOGIN'
        self.screen_height = 800
        self.screen_width = 400
        self.screen = pygame.display.set_mode((self.screen_height, self.screen_width))

    def set_state(self, state):
        self.state = state
    
    def get_state(self):
        return self.state
    
    def handleStateChange(self):
        if self.state == 'LOGIN':
            self.handleLogin(self)
        elif self.state == 'CREATE':
            return self.handleCreateProfile(self)
        elif self.state == 'USER SCORES':
            return self.handleUserScores(self)
        elif self.state == 'HOME':
            return self.handleHomeScreen(self)
        elif self.state == 'NEXT LEVEL':
            return self.handleNextLevel(self)
        elif self.state == 'DEATH':
            return self.handleDeath(self)
        elif self.state == 'SETTINGS':
            return self.handleSettings(self)
        elif self.state == 'SCORES':
            return self.handleHighScores(self)
        elif self.state == 'PAUSE':
            return self.handlePause(self)
        elif self.state == 'QUIT':
            return self.handleQuit(self)



    def handleLogin(self):
        self.state == 'LOGIN'
        self.test_surface = pygame.image.load('game_images/background.png')
        self.test_surface = pygame.transform.scale(self.test_surface, (800, 400)).convert_alpha()
        self.screen.blit(self.test_surface, (0,0))

        # need to create the login page / create a profile page here...
        

    def handleCreateProfile(self):
        print('creating a profile')


    def handleUserScores(self):
        print('viewing user high scores')


    def handleHomeScreen(self):
        print('HOME')


    def handleNextLevel(self):
        print('next level')


    def handleDeath(self):
        print('death')


    def handleSettings(self):
        print('settings')


    def handleHighScores(self):
        print('high scores')



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




    
    
    
        



