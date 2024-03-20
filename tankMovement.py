import pygame

# this is a strategy class aimed at dictating the movement of the enemy tank 

class tankMovement():
    def __init__(self, map, player):
        self.map = map
        self.player = player

    
    def move(self, x, y):
        path = self.generateDfsPath()

# this function will create a list of coordinates leading to the player
# that will move around walls 
    def generateDfsPath(self):
        path = []
        directions = [[0, 10], [10, 0], [0, -10], [-10, 0]]
        print('dfs!')
        
    def check_closer_to_player(self):
        print('checks if coordinate is closer to the player!')
    
    def check_if_coordinate_in_wall(self):
        print('checks if the coordinate is in a wall!')
    



