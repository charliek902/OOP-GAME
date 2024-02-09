# the zombie will act like a finite state machine 

from enemy import enemy
from entity import entity

class zombie(enemy, entity):
    def __init__(self, state, position_x, position_y, health, player):
        self.state = state
        self.position_x = position_x
        self.position_y = position_y
        self.health = health
        self.player = player

    def interpret_state():
        print('interpreting the state of the devil, responds with actions')

    def moveToPlayer():
        print('searches for the player')
    
    def attack():
        print('attacks!')

    def update():
        print('update!')
        # will probably need to update the position of the player in update 

