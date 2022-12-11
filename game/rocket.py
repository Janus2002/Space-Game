import pygame

class Rocket:
    def __init__(self):
        self.rImg = pygame.image.load("Data/images/bullet.png") 
        self.x = 0
        self.y = 0
        self.rRect = self.rImg.get_rect()
        self.vX = 15
        self.vY = 0
    #Ready is the rocket not the on screen | "fire" rocket is fired onto the screen (moving)
        self.rstate = "ready"
        self.rRect.x = -40
        self.rRect.y = -40