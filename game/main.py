import pygame

#Initialize the program
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Game")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("battleship.png")
playerX = 80
playerY = 268
playerVelocityY = 0
playerVelocityX = 0

def player():
    #Drawing image onto screen (blit)
    screen.blit(playerImg, (playerX,playerY))

#running the window
running = True
while running:

    #RGB colours (RED,GREEN,BLUE)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Checks if a button the keboard was pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerVelocityX += 0.2

            if event.key == pygame.K_DOWN:
                playerVelocityX -= 0.2

            if event.key == pygame.K_RIGHT:
                playerVelocityY += 0.2

            if event.key == pygame.K_LEFT:
                playerVelocityY -= 0.2

        #Waits until keyboard button is released to stop
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerVelocityY = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerVelocityX = 0

    #Inserting border boundries for X
    if playerX <= 0:
        playerX = 0
    elif playerX >= 668:
        playerX = 668
    
    #Inserting border boundries for Y
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    playerY += playerVelocityY
    playerX += playerVelocityX
    player()
    #Update display when there is a change
    pygame.display.update()

#Quit the game after closing
pygame.quit()