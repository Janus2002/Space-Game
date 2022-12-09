import pygame

class Rocket:
    rImg = pygame.image.load("Data/images/bullet.png") 
    X = 0
    Y = 0
    rRect = rImg.get_rect()
    VX = 2
    VY = 0
    #Ready is the rocket not the on screen | "fire" rocket is fired onto the screen (moving)
    rstate = "ready"
    rRect.x = -40
    rRect.y = -40