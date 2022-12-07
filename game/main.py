import math
import pygame

#Initialize the program
pygame.init()

Screen_x = 1280
Screen_y = 720

#create the screen
screen = pygame.display.set_mode((Screen_x,Screen_y))

#Title and Icon
pygame.display.set_caption("Space Game")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)


#Player
playerImg = pygame.image.load("battleship.png")
playerX = 80
playerY = Screen_y/2 -32
playerVelocityY = 0
playerVelocityX = 0

def player():
    #Drawing image onto screen (blit)
    screen.blit(playerImg, (playerX,playerY))

#Background
bg = pygame.image.load("background.png").convert()
bg_width = bg.get_width()
scroll = 0
tiles = math.ceil(Screen_x/bg_width) + 1

#running the window
running = True
while running:

    #RGB colours (RED,GREEN,BLUE)
    screen.fill((0,0,0))

    #Scrolling background
    for i in range(0,tiles):
        screen.blit(bg,(i*bg_width +scroll,0))

    scroll -=0.5

    if abs(scroll) > bg_width:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Checks if a button the keboard was pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerVelocityX += 0.5

            if event.key == pygame.K_DOWN:
                playerVelocityX -= 0.5

            if event.key == pygame.K_RIGHT:
                playerVelocityY += 0.5

            if event.key == pygame.K_LEFT:
                playerVelocityY -= 0.5

        #Waits until keyboard button is released to stop
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerVelocityY = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerVelocityX = 0

    #Inserting border boundries for X
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1180:
        playerX = 1180
    
    #Inserting border boundries for Y
    if playerY <= 0:
        playerY = 0
    elif playerY >= 656:
        playerY = 656

    playerY += playerVelocityY
    playerX += playerVelocityX
    player()
    #Update display when there is a change
    pygame.display.update()

#Quit the game after closing
pygame.quit()