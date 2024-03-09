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
from levelGenerator import levelGenerator
from point_counter import point_counter


# state, position_x, position_y, health, player

player_socket_connection = True
pygame.init()
#LOGIN MENU gets rendered below...
renderer = Renderer()

# we need to have a level generator --> this would create the enemy tanks 
# (perhaps a factor class depending on the level generator)

game_state = game(renderer, 'active', 800, 400, renderer.screen)
shooter = player('alive', 170, 80, 5, 0, 5, 0, None, game_state)

# level generator will create the enemies 
map_of_game = map(shooter)
# setting the map here... 
shooter.set_map(map_of_game)

game_level_generator = levelGenerator(map_of_game, shooter)
command_handler = keyboardHandler(renderer, shooter)

map_of_game.generate_walls()


# health, x_position, y_position, width, height, points, screen
player_healthbar = healthbar(720, 20, 60 ,10, 100, game_state.test_surface, shooter)
player_info_counter = point_counter(20, 20, 0)


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
      shooter.update()
      shooter.update_player_bullets()
      game_level_generator.update()
      map_of_game.update_walls()
      player_info_counter.update(game_state.points, game_level_generator.level, game_level_generator.remaining_enemy_tanks)
      
      


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





