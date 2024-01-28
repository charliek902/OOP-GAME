import pygame 
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800, 400))
test_surface  = pygame.image.load('game_images/Famous-old-video-game-scene.png.webp')
test_surface = pygame.transform.scale(test_surface, (800, 400)).convert_alpha()


test_font = pygame.font.Font(None,50)


# for importing an image: pygame.image.load('graphics/sky/image.png')
# any kind of graphical import will be its own surface 

# pygame will overlay images depending on which image was last called so keep that in mind!

test__font_surface = test_font.render('My game', False, 'Green')

pacman_surface = pygame.image.load('game_images/Pacman.svg')
pacman_surface = pygame.transform.scale(pacman_surface, (15, 15)).convert_alpha()
pacman_x_position = 170
pacman_y_position = 80
# takes a surface and puts a rectangle around it 
pacman_rec = pacman_surface.get_rect(topleft = (pacman_x_position, pacman_y_position))
first = 1


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
    # this way we can associate the pacman surface with the pac man rectangle
    # to move the image, you move the rectangle rather than the surface itself... 
    pacman_rec.left += 1
    screen.blit(pacman_surface, pacman_rec)
    # printing out rectangle is really useful for dimensions purposes... 
    mouse_position = pygame.mouse.get_pos()
    if pacman_rec.collidepoint((mouse_position)): 
        print('collision' + str(first)) 
        first += 1 

    if pacman_rec.x >= 620: pacman_rec.x  = 170
    pygame.display.update()


