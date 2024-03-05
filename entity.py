from abc import ABC, abstractmethod
import random


class entity(ABC):
    def __init__(self, state, position_x, position_y, health, type):
        self.state = state
        self.position_x = position_x
        self.position_y = position_y
        self.health = health
        self.name = hash(random.randint(0, 10000))
        self.type = type




