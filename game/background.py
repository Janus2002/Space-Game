import pygame
import math

class Background:
    
    def __init__(self):
        self.bg = pygame.image.load("Data/images/background.png").convert()
        self.bgW = self.bg.get_width()
        self.scroll = 0
        self.tiles = math.ceil(1280/self.bgW) + 1