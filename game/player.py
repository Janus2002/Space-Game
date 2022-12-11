import pygame

class Player:
    pImg = pygame.image.load("Data/images/battleship.png")
    pRect = pImg.get_rect()
    x = 80
    y = 328
    vY = 0
    vX = 0
    lives = 5
    pSpeed = 7.5