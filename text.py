import pygame
# this is the button class for each pages

class text():
    def __init__(self, x, y, content, screen):
        self.x = x
        self.y = y
        self.content = content
        self.colour = "blue"
        self.screen = screen
        self.font = pygame.font.SysFont(None, 24)
        self.render()
    
    def render(self):
        img = self.font.render(self.content , True, "blue")
        self.screen.blit(img, (self.x, self.y))

 

