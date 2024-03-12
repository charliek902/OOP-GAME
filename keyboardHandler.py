import pygame

# will probably need to pass in the game state in here and also the main character 

class keyboardHandler():
    def __init__(self, renderer, player):
        self.renderer = renderer
        self.player = player
    def handleEvent(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode == ' ':
                self.player.fire()
        if event.type == pygame.KEYDOWN:
            if event.unicode == '\x1b' or event.unicode == 'q':
                self.renderer.handleQuit()
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'p' and self.renderer.state != 'HOME':
                self.renderer.handlePause()
            elif event.unicode == 'p' and self.renderer.state == 'HOME':
                self.renderer.handlePlay()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and event.key == pygame.K_LEFT:
                self.player.moveDiagonalUpLeft()
            elif event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
                self.player.moveDiagonalUpRight()
            elif event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
                self.player.moveDiagonalDownLeft()
            elif event.key == pygame.K_DOWN and event.key == pygame.K_RIGHT:
                    self.player.moveDiagonalDownRight()
            elif event.key == pygame.K_UP:
                self.player.move_up()
            elif event.key == pygame.K_DOWN:
                self.player.move_down()
            elif event.key == pygame.K_LEFT:
                self.player.move_left()
            elif event.key == pygame.K_RIGHT:
                self.player.move_right()
    
    def handleKeyPress(self, keys):
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.player.moveDiagonalUpRight()
        elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.player.moveDiagonalUpLeft()
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.player.moveDiagonalDownRight()
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.player.moveDiagonalDownLeft()
        elif keys[pygame.K_UP]:
            self.player.move_up()
        elif keys[pygame.K_DOWN]:
            self.player.move_down()
        elif keys[pygame.K_LEFT]:
            self.player.move_left()
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
        
       
        if keys[pygame.K_SPACE]:
            self.player.fire()
                



    


           

    