# the tank will act like a finite state machine 

from enemy import enemy
from entity import entity
import pygame

class tank(enemy, entity):
    def __init__(self, state, position_x, position_y, health, player):
        self.state = state
        self.position_x = position_x
        self.position_y = position_y
        self.health = health
        self.player = player
        self.screen = pygame.display.set_mode((800, 400))
        self.DEFAULT_IMAGE_SIZE = (25, 25)
        self.image = pygame.image.load('game_images/red_tank.png')
        self.image = pygame.transform.scale(self.image, self.DEFAULT_IMAGE_SIZE)
        self.tank_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
    

    def interpret_state():
        print('interpreting the state of the tank, responds with actions')
        # if it's a long distance distance away from the player, it will turn and move towards the player 

    def turnToPlayer():
        print('turns to the player')
 
    def moveToPlayer(self):
        if self.player.position_x < self.position_x and self.player.position_x < 800 and self.player.position_x > 0:
            self.tank_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
            self.tank_rec.x -= 1
            self.position_x = self.tank_rec.x
            self.position_y = self.tank_rec.y
        elif self.player.position_x > self.position_x and self.player.position_x < 800 and self.player.position_x > 0:
            self.tank_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
            self.tank_rec.x += 1
            self.position_x = self.tank_rec.x
            self.position_y = self.tank_rec.y

        if self.player.position_y < self.position_y and self.player.position_y < 400 and self.player.position_y > 0:
            self.tank_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
            self.tank_rec.y -= 1
            self.position_x = self.tank_rec.x
            self.position_y = self.tank_rec.y
        elif self.player.position_y > self.position_y and self.player.position_y < 400 and self.player.position_y > 0:
            self.tank_rec = self.image.get_rect(topleft = (self.position_x, self.position_y))
            self.tank_rec.y += 1
            self.position_x = self.tank_rec.x
            self.position_y = self.tank_rec.y
    
    def check_collide(self):
        if self.position_x == self.player.position_x and self.position_y == self.player.position_y:
            self.player.health -= 1



    
    def attack():
        print('attacks!')
        # NB: this should be firing when at a certain distance 

    def update(self):
        self.moveToPlayer()
        self.check_collide()

        self.screen.blit(self.image, self.tank_rec)