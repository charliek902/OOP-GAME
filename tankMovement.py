import pygame

# this is a strategy class aimed at dictating the movement of the enemy tank 

class tankMovement():
    def __init__(self, map, player, x, y):
        self.map = map
        self.player = player
        self.x = x
        self.y = y

    def generateDfsPath(self, possible_x, possible_y):
        def dfs(possible_x, possible_y):
            distance = self.get_distance_to_player(possible_x, possible_y)
            if distance < 20000:
                return path

            for dx, dy in directions:
                next_x = possible_x + dx
                next_y = possible_y + dy 

                # do need to store the last / previous distance that was recorde... 
                if self.check_closer_to_player(next_x, next_y) and not self.check_if_coordinate_in_wall(next_x, next_y):
                    path.append([next_x, next_y])
                    return dfs(next_x, next_y)
            path.pop()
       
        path = []
        path.append([possible_x, possible_y])
        # DIRECTIONS TO GO RIGHT, DOWN, LEFT AND UP 10 PIXELS 
        directions = [[0, 10], [10, 0], [0, -10], [-10, 0]]
        return dfs(possible_x, possible_y)

    
        
    def check_closer_to_player(self, next_x, next_y):
        print('checks if coordinate is closer to the player!')
        return True
    
    def check_if_coordinate_in_wall(self, next_x, next_y):
        print('checks if the coordinate is in a wall!')
        return False

    def get_distance_to_player(self, x, y):
        # returns the manhattan distace to the player 
        return ((self.player.position_x - x) * (self.player.position_x - x)) \
        + ((self.player.position_y - y) * (self.player.position_y - y))
    

# TANK SHOULD GET COORDINATES, TURN TOWARDS THEM UNTIL DISTANCE ---> THEN TANK SHOULD AIM AND FIRE AT ENEMY 
    



