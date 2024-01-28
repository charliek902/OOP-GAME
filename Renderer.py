class Renderer():
    def __init__(self):
        self.state = 'HOME'

    def set_state(self, state):
        self.state = state
    
    def get_state(self):
        return self.state
    
    def handleStateChange(self):
        if self.state == 'HOME':
            return self.handleHomeScreen(self)
        elif self.state == 'NEXT LEVEL':
            return self.handleNextLevel(self)
        elif self.state == 'DEATH':
            return self.handleDeath(self)
        elif self.state == 'SETTINGS':
            return self.handleSettings(self)
        elif self.state == 'SCORES':
            return self.handleHighScores(self)


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
        
        
        
    # here we would need to create the correct buttons etc for the home screen, death screen, next level etc 
    # there is also settings 



