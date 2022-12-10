import random as rd, pygame, math
from player import Player
from background import Background
from enemy import Enemy
from rocket import Rocket

#Initialize the program
def main():
    pygame.init()

    Screen_x = 1280
    Screen_y = 720

    #create the screen
    SCREEN = pygame.display.set_mode((Screen_x,Screen_y))

    #Title and Icon
    pygame.display.set_caption("Space Game")
    icon = pygame.image.load("Data/images/spaceship.png")
    pygame.display.set_icon(icon)

    #Player
    player = Player()
    pSpeed = 0.75
    score = 0

    #Enemy
    enemy = Enemy()
    numOfEnemies = 7 
    enemy.enemies(numOfEnemies)

    #Rocekt
    rocket = Rocket()
    def fireRocket(x,y):
        rocket.rstate = "fire"
        SCREEN.blit(rocket.rImg, (x+96,y+34))
        rocket.rRect.y = y

    #Background
    bg = Background()

    #running the window
    running = True
    while running:

        #RGB colours (RED,GREEN,BLUE)
        SCREEN.fill((0,0,0))

    #Scrolling background
        for i in range(0,bg.tiles):
            SCREEN.blit(bg.bg,(i*bg.bgW +bg.scroll,0))

        bg.scroll -=0.5

        if abs(bg.scroll) > bg.bgW:
            bg.scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Checks if a button the keboard was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.VX += pSpeed

                if event.key == pygame.K_DOWN:
                    player.VX -= pSpeed

                if event.key == pygame.K_RIGHT:
                    player.VY += pSpeed

                if event.key == pygame.K_LEFT:
                    player.VY -= pSpeed
                    
                if event.key == pygame.K_SPACE:
                    #Cannot fire spam
                    if rocket.rstate == "ready":
                        rocket.Y = player.Y
                        rocket.X = player.X
                        fireRocket(rocket.X, rocket.Y)

            #Waits until keyboard button is released to stop
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.VY = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.VX = 0
            
    #Inserting border boundries for X
        if player.X <= 0:
            player.X = 0
        elif player.X >= 1148:
            player.X = 1148
    
    #Inserting border boundries for Y
        if player.Y <= 0:
            player.Y = 0
        elif player.Y >= 624:
            player.Y = 624

        player.Y += player.VY
        player.X += player.VX
        player.pRect.x = player.X
        player.pRect.y = player.Y
    
    #Enemy Movement
        for i in range(numOfEnemies):
            enemy.Y[i] += enemy.VY[i]
            enemy.eRect[i].x = enemy.X[i]
            enemy.eRect[i].y = enemy.Y[i]

            if enemy.Y[i] < 0:
                enemy.VY[i] = 1
                enemy.X[i] -= enemy.VX[i]
            elif enemy.Y[i] >= 654:
                enemy.VY[i] = -1
                enemy.X[i] -= enemy.VX[i]
            
            if rocket.rRect.colliderect(enemy.eRect[i]):
                rocket.rstate = "ready"
                score += 10
                enemy.X[i] = rd.randint(640,1100)
                enemy.Y[i] = rd.randint(0,654)
                print(score)
                rocket.rRect.x = -40
                rocket.rRect.y = -40
            SCREEN.blit(enemy.eImg[i], (enemy.X[i],enemy.Y[i]))

        #Rocket Movement
        if rocket.X >= 1148:
            rocket.rstate = "ready"
            rocket.rRect.x = -40
            rocket.rRect.y = -40
        if rocket.rstate == "fire":
            fireRocket(rocket.X,rocket.Y)
            rocket.X += rocket.VX
            rocket.rRect.x = rocket.X + 96
            rocket.rRect.y = rocket.Y + 34
            
        SCREEN.blit(player.pImg, (player.X,player.Y))
       
        #Update display when there is a change
        pygame.display.update()

    #Quit the game after closing
    pygame.quit()

if __name__ == "__main__":
    main()