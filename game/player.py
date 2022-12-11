import pygame

class Player:
    def __init__(self,x,y):
        self.pImg = pygame.image.load("Data/images/battleship.png")
        self.pRect = self.pImg.get_rect()
        self.x = x
        self.y = y
        self.vY = 0
        self.vX = 0
        self.lives = 5
        self.pSpeed = 7.5