import pygame

# this is a strategy class aimed at dictating the movement of the enemy tank 

class tankMovement():
    def __init__(self, map):
        self.map = map

    
    def move(self, x, y):
        self.generate_path()


    def generate_path(self):
        if self.generate_shortest_path():
            return self.generate_shortest_path()
        else:
            return self.generate_dfs_path()


    def generate_shortest_path(self):
        print('generates the shortest path')
        # check if there are any walls between the tank and the player 



        # need to check if entities are within this shortest path 
        # if they are not --> coordinates are needed to be produced for the tanks to go to 

        # probably just need to geneate the next coordinate   

    def generate_dfs_path(self):
        print('generates a dfs path')
        # this path should go around other tanks and walls 

