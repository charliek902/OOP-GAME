import pygame 
import os.path
import sys
from Renderer import Renderer
from keyboardHander import keyboardHander
from entity import entity
#sys.path.append(os.path.join(os.path.dirname(__file__), 'Renderer.py'))

#import matplotlib.pyplot as plt
#import cv2

pygame.init()
renderer = Renderer()
print(renderer.state)

# before the loop we need to initialize all the objects - the enemies, the walls, the player, health, health bar, guns
# bullets, background image, keyboard handler and renderer, maybe also music and sound effects 





screen_height = 800
screen_width = 400

screen = pygame.display.set_mode((screen_height, screen_width))
test_surface  = pygame.image.load('game_images/background.png')
test_surface = pygame.transform.scale(test_surface, (800, 400)).convert_alpha()

shooter = pygame.image.load('game_images/shooter.png')
shooter = pygame.transform.scale(shooter, (25, 25)).convert_alpha()
shooter_x_position = 170
shooter_y_position = 80
# takes a surface and puts a rectangle around it 
shooter_rec = shooter.get_rect(topleft = (shooter_x_position, shooter_y_position))
first = 1
gravity = 0


while True: 
    # draw all our elements 
    # update everything 

    # check for all possible type of player input 
    for event in pygame.event.get():

        # we should pass in the event into a keyboard handler class that will deal with the resultant logic...


        # we could have a class which is like a keyboard handler to handle the key changes... 

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # to make the player go up every time you click on it 
      #  if event.type == pygame.MOUSEBUTTONDOWN:
        #    if shooter_rec.collidepoint(event.pos):
          #      gravity -= 15

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('space pressed')
            #    gravity -= 10
            else:
                print('key pressed!')
        if event.type == pygame.KEYUP:
            print('key up!')
        mouse_position = pygame.mouse.get_pos()
       # if shooter_rec.collidepoint((mouse_position)): 
       #     print('collision' + str(first)) 
       #     first += 1 

    screen.blit(test_surface, (0,0))
    # this way we can associate the shooter surface with the pac man rectangle
    # to move the image, you move the rectangle rather than the surface itself... 
 #   shooter_rec.left += 1
    screen.blit(shooter, shooter_rec)
  #  gravity += 1


    # printing out rectangle is really useful for dimensions purposes...

  #  if shooter_rec.x >= 620: shooter_rec.x  = 170
  #  shooter_rec.y += gravity
  #  if shooter_rec.y >= 400: 
   #     shooter_rec.y  = 80
   #     shooter_rec.x  = 170
    #    gravity = 0

    clock = pygame.time.Clock()
    FPS = 60  # Set your desired frames per second
    clock.tick(FPS)

    pygame.display.update()







# Notes

#test_font = pygame.font.Font(None,50)

#def create_2d_array(x, y):
 #   two_d = [[0 for x in range(x)] for y in range(y)]
   # return two_d

#two_d = create_2d_array(screen_height, screen_width)

#path= 'game_images/Famous-old-video-game-scene.png.webp'

#img= cv2.imread(path)

#cv2.imshow('image', img)

#imgMat= np.random.rand(100,100)

#plt.imshow(imgMat,'gray')#omot gray if output required isn’t grayscale

#plt.show()


# for importing an image: pygame.image.load('graphics/sky/image.png')
# any kind of graphical import will be its own surface 

# pygame will overlay images depending on which image was last called so keep that in mind!

#test__font_surface = test_font.render('My game', False, 'Green') 
    
# screen.blit(test__font_surface, (300, 50))


