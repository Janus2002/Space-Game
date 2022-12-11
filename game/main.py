import random as rd, pygame
from player import Player
from background import Background
from enemy import Enemy
from rocket import Rocket
from score import Score
from pygame import mixer

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

    #Background music
    mixer.music.load("Data/sounds/background.wav")
    mixer.music.play(-1)

    #Player
    player = Player()
    pSpeed = 0.75

    #Score
    score = Score()
    font = pygame.font.Font(None, 32)
    def showScore(x,y):
        text = font.render("Score: "+str(score.score), True, (255,255,255))
        SCREEN.blit(text, (x, y))

    #Game over
    over = pygame.font.Font(None, 128)
    def game_over_text():
        text = over.render("GAME OVER", True, (255,255,255))
        SCREEN.blit(text, (360,320))


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
    alive = True
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
            if alive:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.vX += pSpeed

                    if event.key == pygame.K_DOWN:
                        player.vX -= pSpeed

                    if event.key == pygame.K_RIGHT:
                        player.vY += pSpeed

                    if event.key == pygame.K_LEFT:
                        player.vY -= pSpeed
                    
                    if event.key == pygame.K_SPACE:
                    #Cannot fire spam
                        if rocket.rstate == "ready":
                            rocket_sound = mixer.Sound("Data/sounds/laser.wav")
                            rocket_sound.play()
                            rocket.y = player.y
                            rocket.x = player.x
                            fireRocket(rocket.x, rocket.y)

                #Waits until keyboard button is released to stop
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player.vY = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player.vX = 0
            
    #Inserting border boundries for X
        if player.x <= 0:
            player.x = 0
        elif player.x >= 1148:
            player.x = 1148
    
    #Inserting border boundries for Y
        if player.y <= 0:
            player.y = 0
        elif player.y >= 624:
            player.y = 624

        player.y += player.vY
        player.x += player.vX
        player.pRect.x = player.x
        player.pRect.y = player.y
    
    #Enemy Movement
        for i in range(numOfEnemies):
            #Game over
            if enemy.x[i] < 120:
                for j in range(numOfEnemies):
                    enemy.x[j] = -300
                    enemy.y[j] = -300
                    enemy.eRect[j].x = enemy.x[j]
                    enemy.eRect[j].y = enemy.y[j]
                game_over_text()
                break

            if alive:    
                enemy.y[i] += enemy.vY[i]
                enemy.eRect[i].x = enemy.x[i]
                enemy.eRect[i].y = enemy.y[i]

                if enemy.y[i] < 0:
                    enemy.vY[i] = 0.5 
                    enemy.x[i] -= enemy.vX[i]
                elif enemy.y[i] >= 654:
                    enemy.vY[i] = -0.5
                    enemy.x[i] -= enemy.vX[i]
            
            if rocket.rRect.colliderect(enemy.eRect[i]):
                killed = mixer.Sound("Data/sounds/invaderkilled.wav")
                killed.play()
                rocket.rstate = "ready"
                enemy.x[i] = rd.randint(640,1100)
                enemy.y[i] = rd.randint(0,654)
                rocket.rRect.x = -40
                rocket.rRect.y = -40
                score.score += 10
            
            #Player collision with enemy
            if player.pRect.colliderect(enemy.eRect[i]):
                enemy.x[i] = rd.randint(640,1100)
                enemy.y[i] = rd.randint(0,654)
                enemy.eRect[i].x = enemy.x[i]
                enemy.eRect[i].y = enemy.y[i]
                player.lives -= 1
                break
            if player.lives == 0:
                alive = False
                player.vY = 0
                player.vX = 0
                game_over_text()

            SCREEN.blit(enemy.eImg[i], (enemy.x[i],enemy.y[i]))

        #Rocket Movement
        if rocket.x >= 1148:
            rocket.rstate = "ready"
            rocket.rRect.x = -40
            rocket.rRect.y = -40
        if rocket.rstate == "fire":
            fireRocket(rocket.x,rocket.y)
            rocket.x += rocket.vX
            rocket.rRect.x = rocket.x + 96
            rocket.rRect.y = rocket.y + 34

            
        SCREEN.blit(player.pImg, (player.x,player.y))
        showScore(score.x, score.y)
       
        #Update display when there is a change
        pygame.display.update()

    #Quit the game after closing
    pygame.quit()

if __name__ == "__main__":
    main()