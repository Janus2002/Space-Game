import pygame
import random as rd

class Enemy:
    def __init__(self):    
        self.eImg = []
        self.x = []
        self.y = []
        self.eRect = []
        self.vY = []
        self.vX = []
        self.speed = 5

    #To spawn multiple enemies
    def enemies(self,n):
        for i in range(n):
            self.eImg.append(pygame.image.load("Data/images/alien.png"))
            self.x.append(rd.randint(600,1100))
            self.y.append(rd.randint(0,654))
            self.eRect.append(self.eImg[i].get_rect())
            self.vY.append(self.speed)
            self.vX.append(40)