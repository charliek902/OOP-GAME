from entity import entity

# this is a strategy class aimed at dictating the movement of the enemy tank 

class tankMovement(entity):
    def __init__(self, map, entity):
        self.map = map
        self.entity = entity
    
    def move(self):
        self.generate_path()


    def generate_path(self):
        if self.generate_shortest_path():
            return self.generate_shortest_path()
        else:
            return self.generate_dfs_path()



    def generate_shortest_path(self):
        print('generates the shortest path')

        # need to check if entities are within this shortest path 
        # if they are not --> coordinates are needed to be produced for the tanks to go to 

        # probably just need to geneate the next coordinate   

    def generate_dfs_path(self):
        print('generates a dfs path')
        # this path should go around other tanks and walls 

