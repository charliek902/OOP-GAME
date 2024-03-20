from entity import entity
from abc import ABC, abstractmethod 

class enemy(entity):
    def __init__(self, state, position_x, position_y, health, player):
        self.state = state
        self.position_x = position_x
        self.position_y = position_y
        self.health = health
        self.player = player

    @abstractmethod
    def moveToPlayer():
        print('searches for the player')

    @abstractmethod
    def fire():
        print('attacks!')

    @abstractmethod
    def update():
        print('update!')


