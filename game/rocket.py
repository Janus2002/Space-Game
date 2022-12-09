import pygame
from player import Player

class Rocket:
    rImg = pygame.image.load("bullet.png")
    X = Player.X +96
    Y = Player.Y + 34
    VX = 20
    VY = 0
    #Ready is the rocket not the on screen | "fire" rocket is fired onto the screen (moving)
    rstate = "ready"