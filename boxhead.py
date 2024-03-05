import pygame 
import os.path
import sys
from Renderer import Renderer
from keyboardHandler import keyboardHandler
from entity import entity
from player import player
from game import game
from healthbar import healthbar
from tank import tank
from map import map


# state, position_x, position_y, health, player

player_socket_connection = True
pygame.init()
#LOGIN MENU gets rendered below...
renderer = Renderer()

# we need to have a level generator --> this would create the enemy tanks 
# (perhaps a factor class depending on the level generator)

game_state = game(renderer, 'active', 800, 400, renderer.screen)
shooter = player('alive', 170, 80, 5, 0, 5, 0)
# level generator will create the enemies 

map_of_game = map(shooter)

easy_tank = tank('SEARCH', 150, 150, 100, shooter, map_of_game, 'TANK')
medium_tank = tank('SEARCH', 300, 300, 100, shooter, map_of_game, 'TANK')

map_of_game.add_entity(easy_tank)
map_of_game.add_entity(medium_tank)


command_handler = keyboardHandler(renderer, shooter)

# health, x_position, y_position, width, height, points, screen

player_healthbar = healthbar(720, 20, 60 ,10, 100, game_state.test_surface, shooter)
print(renderer.state)

# before the loop we need to initialize all the objects - the enemies, the walls, the player, health, health bar, guns
# bullets, background image, keyboard handler and renderer, maybe also music and sound effects 


# takes a surface and puts a rectangle around it 

first = 1
gravity = 0

#renderer.set_state('PLAY')

while player_socket_connection: 
    # draw all our elements 
    # update everything 

    # check for all possible type of player input 
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        command_handler.handleEvent(event)
        
        
    if game_state.renderer.state == 'PLAY':
      command_handler.handleKeyPress(keys)
      player_healthbar.display()
      game_state.update()
      easy_tank.update()
      medium_tank.update()
      shooter.update()

    elif game_state.renderer.state == 'LOGIN':
      game_state.renderer.handleLogin()
    elif game_state.renderer.state == 'CREATE':
      game_state.renderer.handleCreateProfile()
    elif game_state.renderer.state == 'USER SCORES':
      game_state.renderer.handleUserScores()
      

    clock = pygame.time.Clock()
    FPS = 60  # Set your desired frames per second
    clock.tick(FPS)

    pygame.display.update()

"""
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
        elif self.state == 'PAUSE':
            return self.handlePause(self)
        elif self.state == 'QUIT':
            return self.handleQuit(self) """




