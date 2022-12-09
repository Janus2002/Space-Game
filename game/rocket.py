import pygame

class Rocket:
    rImg = pygame.image.load("Data/images/bullet.png")
    X = 0
    Y = 0
    VX = 1
    VY = 0
    #Ready is the rocket not the on screen | "fire" rocket is fired onto the screen (moving)
    rstate = "ready"