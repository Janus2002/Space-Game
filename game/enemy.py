import pygame
import random as rd

class Enemy:
    eImg = []
    x = []
    y = []
    eRect = []
    vY = []
    vX = []
    speed = 5

    #To spawn multiple enemies
    def enemies(self,n):
        for i in range(n):
            self.eImg.append(pygame.image.load("Data/images/alien.png"))
            self.x.append(rd.randint(720,1100))
            self.y.append(rd.randint(0,654))
            self.eRect.append(self.eImg[i].get_rect())
            self.vY.append(self.speed)
            self.vX.append(40)