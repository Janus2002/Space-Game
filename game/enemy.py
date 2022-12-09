import pygame
import random as rd

class Enemy:
    eImg = pygame.image.load("Data/images/alien.png")
    X = rd.randint(640,1100)
    Y = rd.randint(0,654)
    VY = 0.3
    VX = 40