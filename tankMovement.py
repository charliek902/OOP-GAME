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
                if self.check_closer_to_player(next_x, next_y, distance) and not self.check_if_coordinate_in_wall(next_x, next_y):
                    path.append([next_x, next_y])
                    return dfs(next_x, next_y)
                
            if len(path) > 0: path.pop()
       
        path = []
        path.append([possible_x, possible_y])
        # DIRECTIONS TO GO RIGHT, DOWN, LEFT AND UP 10 PIXELS 
        directions = [[0, 10], [10, 0], [0, -10], [-10, 0]]
        return dfs(possible_x, possible_y)

    
        
    def check_closer_to_player(self, next_x, next_y, prev_distance):
        if self.get_distance_to_player(next_x, next_y) < prev_distance:
            return True
        return False

    def check_if_coordinate_in_wall(self, next_x, next_y):
        walls = self.map.get_wall_locations()
        for wall in walls:
            # check if postion x <= next_x <= check postion x + wall length and 
            # check if postion y <= next_y <= check postion y + wall length  
            # if so for one wall then return True
            return True
            

        return False

    def get_distance_to_player(self, x, y):
        # returns the manhattan distace to the player 
        return ((self.player.position_x - x) * (self.player.position_x - x)) \
        + ((self.player.position_y - y) * (self.player.position_y - y))
    



