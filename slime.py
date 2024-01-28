import pygame 
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800, 400))
test_surface  = pygame.Surface((100, 200))
test_surface.fill('Red')

test_font = pygame.font.Font(None,50)


# for importing an image: pygame.image.load('graphics/sky/image.png')
# any kind of graphical import will be its own surface 


# pygame will overlay images depending on which image was last called so keep that in mind!

test__font_surface = test_font.render('My game', False, 'Green')

pacman_surface = pygame.image.load('game_images/Pacman.svg')
pacman_surface = pygame.transform.scale(pacman_surface, (20, 20))

pacman_x_position = 0
pacman_y_position = 0



while True: 
    # draw all our elements 
    # update everything 

    # check for all possible type of player input 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (0,0))
    screen.blit(test__font_surface, (300, 50))
    screen.blit(pacman_surface, (pacman_x_position, pacman_y_position))
    pacman_x_position += 1
    if pacman_x_position > 700 or pacman_y_position > 400:
        pacman_x_position = 0
        pacman_y_position = 0
    pygame.display.update()
