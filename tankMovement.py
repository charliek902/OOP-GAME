import pygame

# this is a strategy class aimed at dictating the movement of the enemy tank 

class tankMovement():
    def __init__(self, map, player, x, y):
        self.map = map
        self.player = player
        self.x = x
        self.y = y

    def generateDfsPath(self, possible_x, possible_y):
        path = []
        path.append([possible_x, possible_y])
        # DIRECTIONS 
        directions = [[0, -5], [-5, 0], [0, 5], [5, 0]]
        
        def dfs(possible_x, possible_y, directions):
            distance = self.get_distance_to_player(possible_x, possible_y)
            if distance <= 50:
                return path

            for dx, dy in directions:
                next_x = possible_x + dx
                next_y = possible_y + dy 

                if self.check_closer_to_player(next_x, next_y, distance):
                    path.append([next_x, next_y])
                    return dfs(next_x, next_y, directions)

        return dfs(possible_x, possible_y, directions)

    def check_closer_to_player(self, next_x, next_y, prev_distance):
        current_distace = self.get_distance_to_player(next_x, next_y)
        if current_distace < prev_distance:
            return True
        return False

    def get_distance_to_player(self, x, y):
        # Returns the Manhattan distance to the player
        return abs(self.player.position_x - x) + abs(self.player.position_y - y)

    



