import pygame

# will probably need to pass in the game state in here and also the main character 

class keyboardHandler():
    def __init__(self, renderer, player):
        self.renderer = renderer
        self.player = player
    def handleEvent(self, event):
        if event.type == pygame.QUIT:
            print('game quits!')
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode == ' ':
                self.player.fire()
        if event.type == pygame.KEYDOWN:
            if event.unicode == '\x1b' or event.unicode == 'q':
                self.renderer.handleQuit()
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'p':
                self.renderer.handlePause()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player.move_up()
            if event.key == pygame.K_DOWN:
                self.player.move_down()
            if event.key == pygame.K_LEFT:
                self.player.turn_left()
            if event.key == pygame.K_RIGHT:
                self.player.turn_right()
    
    def handleKeyPress(self, keys):
        if keys[pygame.K_UP]:
            self.player.move_up()
        if keys[pygame.K_DOWN]:
            self.player.move_down()
        if keys[pygame.K_LEFT]:
            self.player.turn_left()
        if keys[pygame.K_RIGHT]:
            self.player.turn_right()
                
       #### if keys[pygame.K_LEFT]:
         ###   self.player.turn_left()
       ## if keys[pygame].K_RIGHT:
          #  self.player.turn_right()


    


           

    