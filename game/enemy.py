import pygame
import random as rd

class Enemy:
    eImg = []
    X = []
    Y = []
    eRect = []
    VY = []
    VX = []

    #To spawn multiple enemies
    def enemies(self,n):
        for i in range(n):
            self.eImg.append(pygame.image.load("Data/images/alien.png"))
            self.X.append(rd.randint(640,1100))
            self.Y.append(rd.randint(0,654))
            self.eRect.append(self.eImg[i].get_rect())
            self.VY.append(1)
            self.VX.append(40)