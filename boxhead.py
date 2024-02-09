import pygame 
import os.path
import sys
from Renderer import Renderer
from keyboardHandler import keyboardHandler
from entity import entity
from player import player
from game import game
from healthbar import healthbar

# construcing all the necessary objects to play the game... 
pygame.init()
renderer = Renderer()
game_state = game(renderer, 'active', 800, 400)
shooter = player('alive', 170, 80, 10, -90, 90, 0)
command_handler = keyboardHandler(renderer, shooter)

# health, x_position, y_position, width, height, points, screen

player_healthbar = healthbar(720, 20, 60 ,10, 100, game_state.test_surface, shooter)
print(renderer.state)

# before the loop we need to initialize all the objects - the enemies, the walls, the player, health, health bar, guns
# bullets, background image, keyboard handler and renderer, maybe also music and sound effects 


# takes a surface and puts a rectangle around it 

first = 1
gravity = 0

while True: 
    # draw all our elements 
    # update everything 

    # check for all possible type of player input 
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        command_handler.handleEvent(event)
        




    command_handler.handleKeyPress(keys)
    player_healthbar.display()
    game_state.update()
    shooter.update()
    pygame.event.pump()
        
       # if shooter_rec.collidepoint((mouse_position)): 
       #     print('collision' + str(first)) 
       #     first += 1 


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




