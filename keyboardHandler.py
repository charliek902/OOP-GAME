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
            print('true')
            self.player.move_up()
        if keys[pygame.K_DOWN]:
            print('true')
            self.player.move_down()


    


           
   ##     elif event.type == pygame.KEYUP:
            
            #mouse_position = pygame.mouse.get_pos()
    #    elif event.type == pygame.


    #    else:
            # there should be a handling of controls (arrow keys)
          ###  print('handle!')
            # if not arrow arrow keys, check if the keys p or q are pressed 
         ##   print('pause or quit')
            # if not those keys check if any numbers are pressed (will handle the cases when weapons are swapped)
         #   print('weapon change')


    