import pygame
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
from game_info import game_info

# Construction of all the necessary classes to start the game...
def initialize_game():
    player_socket_connection = True
    pygame.init()
    renderer = Renderer('HOME')
    game_state = game(renderer, 'active', 800, 400, renderer.screen)
    shooter = player('alive', 170, 80, 5, 0, 5, 0, None, game_state)
    map_of_game = map(shooter)
    shooter.set_map(map_of_game)
    game_level_generator = levelGenerator(map_of_game, shooter)
    command_handler = keyboardHandler(renderer, shooter)
    map_of_game.generate_walls()
    player_healthbar = healthbar(720, 20, 60, 10, 100, game_state.test_surface, shooter)
    player_info = game_info(20, 20, 0, renderer)

    return player_socket_connection, renderer, game_state, shooter, map_of_game, game_level_generator, command_handler, player_healthbar, player_info

# Restart function
def restart_game():
    return initialize_game()

# Main game loop
def main():
    player_socket_connection, renderer, game_state, shooter, map_of_game, game_level_generator, command_handler, player_healthbar, player_info = initialize_game()

    while player_socket_connection:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            command_handler.handleEvent(event)

            # Checks for the restart condition...
            if shooter.state == 'DEATH' and renderer.state != 'DEATH':
                renderer.set_state('DEATH')
                renderer.handleStateChange()
            elif shooter.state == 'DEATH' and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                player_socket_connection, renderer, game_state, shooter, map_of_game, game_level_generator, command_handler, player_healthbar, player_info = restart_game()

        if game_state.renderer.state == 'HOME' or game_state.renderer.state == 'QUIT':
            renderer.handleStateChange()
        elif game_state.renderer.state == 'PLAY':
            command_handler.handleKeyPress(keys)
            player_healthbar.display()
            game_state.update()
            shooter.update()
            shooter.update_player_bullets()
            game_level_generator.update()
            map_of_game.update_walls()
            player_info.update(game_state.points, game_level_generator.level, game_level_generator.remaining_enemy_tanks)

        clock = pygame.time.Clock()
        FPS = 60
        clock.tick(FPS)

        pygame.display.update()

if __name__ == "__main__":
    main()
