# the devil will act like a finite state machine 

from enemy import enemy
from entity import entity

class devil(enemy, entity):
    def __init__(self, state, position_x, position_y, health, player):
        self.state = state
        self.position_x = position_x
        self.position_y = position_y
        self.health = health
        self.player = player
    

    def interpret_state():
        print('interpreting the state of the devil, responds with actions')
        # if it's a long distance distance away from the player, it will turn and move towards the player 

    def turnToPlayer():
        print('turns to the player')

    def moveToPlayer():
        print('searches for the player')
    
    def attack():
        print('attacks!')
        # NB: this should be firing when at a certain distance 

    def update():
        print('update!')