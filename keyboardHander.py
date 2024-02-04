
# will probably need to pass in the game state in here and also the main character 

class keyboardHander():
    def __init__(self, renderer):
        self.renderer = renderer
    def handleEvent(self, event):
        # there should be a handling of controls (arrow keys)
        print('handle!')
        # if not arrow arrow keys, check if the keys p or q are pressed 
        print('pause or quit')
        # if not those keys check if any numbers are pressed (will handle the cases when weapons are swapped)
        print('weapon change')


    