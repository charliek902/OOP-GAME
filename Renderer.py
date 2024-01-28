# this class handles page renderering from different changes in state of the Game

class Renderer():
    def __init__(self):
        self.state = 'LOGIN'

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
        elif self.state == 'PLAY':
            return self.handlePlay(self)

    def handleLogin(self):
        print('LOGIN page')
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
    def handlePlay(self):
        print('play!')
        



