import pygame

class Rocket:
    rImg = pygame.image.load("Data/images/bullet.png") 
    x = 0
    y = 0
    rRect = rImg.get_rect()
    vX = 2
    vY = 0
    #Ready is the rocket not the on screen | "fire" rocket is fired onto the screen (moving)
    rstate = "ready"
    rRect.x = -40
    rRect.y = -40