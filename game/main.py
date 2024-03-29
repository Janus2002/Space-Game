import random as rd, pygame,sys
from player import Player
from background import Background
from enemy import Enemy
from rocket import Rocket
from score import Score
from pygame import mixer

Screen_x, Screen_y = 1280,720
#create the screen
SCREEN = pygame.display.set_mode((Screen_x,Screen_y))

#Setting the FPS
FPS = 60

#Initialize the program
def main():
    pygame.init()

    #Title and Icon
    pygame.display.set_caption("Space Game")
    icon = pygame.image.load("Data/images/spaceship.png")
    pygame.display.set_icon(icon)

    #Background music
    mixer.music.load("Data/sounds/background.wav")
    mixer.music.play(-1)

    #Start Screen
    start = pygame.font.Font("Data/fonts/Cybersky.otf", 128)
    press = pygame.font.Font("Data/fonts/DeathStar.ttf", 32)
    def showStart():
        text = start.render("SPACE GAME!", True, (255,255,255))
        enter = press.render("PRESS 'S' BUTTON TO START",True, (255,255,255))
        SCREEN.blit(text, (280,230))
        SCREEN.blit(enter, (430,360))

    #Player
    player = Player(80,328)
    lives = pygame.font.Font("Data/fonts/RobotInvader.ttf", 22)
    def showLives(x,y):
        text = lives.render("Lives Left: "+str(player.lives), True, (255,255,255))
        SCREEN.blit(text, (x,y))

    #Score
    score = Score()
    font = pygame.font.Font("Data/fonts/RobotInvader.ttf", 22)
    def showScore(x,y):
        text = font.render("Score: "+str(score.score), True, (255,255,255))
        SCREEN.blit(text, (x, y))

    #Game over
    over = pygame.font.Font("Data/fonts/DeathStar.ttf", 96)
    restart = pygame.font.Font("Data/fonts/DeathStar.ttf", 32)
    def game_over_text():
        text = over.render("GAME OVER", True, (255,255,255))
        SCREEN.blit(text, (330,280))
        press = restart.render("PRESS 'R' TO RESTART", True, (255,255,255))
        SCREEN.blit(press, (450,400))

    #Enemy
    enemy = Enemy()
    numOfEnemies = 30
    enemy.enemies(numOfEnemies)

    #Rocekt
    rocket = Rocket()
    def fireRocket(x,y):
        rocket.rstate = "fire"
        SCREEN.blit(rocket.rImg, (x+96,y+34))
        rocket.rRect.y = y

    #Background
    bg = Background()
    scroll = 5
    #running the windows
    alive = False
    start_screen = True
    clock = pygame.time.Clock()


    while True:
        #Loop can only run 60 times within a second
        clock.tick(FPS)
    #Scrolling background
        if alive or start_screen:
            for i in range(0,bg.tiles):
                SCREEN.blit(bg.bg,(i*bg.bgW +bg.scroll,0))
            
            bg.scroll -= scroll
 
            if abs(bg.scroll) > bg.bgW:
                bg.scroll = 0
        else:
            SCREEN.blit(bg.bg,(0,0))

        #Opens the start screen first
        if start_screen:
            showStart()

        #Increases speed of the game
        if score.score % 300 == 0  and score.score != 0:
            rocket.vX += 0.15  
            enemy.speed += 0.25 
            player.pSpeed += 0.05
            score.score += 10
            scroll += 1
         

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            
            #If s is pressed it starts the game
            if start_screen:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        start_screen = False
                        alive = True
            
            #If the player died pressing R will restart the game
            if not alive:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        #Reset all values
                        alive = True
                        player.x = 80
                        player.y= 328
                        player.lives = 5
                        score.score = 0
                        player.pSpeed = 7.5
                        enemy.speed = 5
                        rocket.vX = 15
                        scroll = 5
                        for i in range(numOfEnemies):
                            enemy.x[i] = rd.randint(720,1100)
                            enemy.y[i] = rd.randint(0,654)

            #Checks if a button the keboard was pressed
            if alive:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.vX += player.pSpeed

                    if event.key == pygame.K_DOWN:
                        player.vX -= player.pSpeed

                    if event.key == pygame.K_RIGHT:
                        player.vY += player.pSpeed

                    if event.key == pygame.K_LEFT:
                        player.vY -= player.pSpeed
                    
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
                    enemy.x[j] = rd.randint(600,1100)
                    enemy.y[j] = rd.randint(0,654)
                    enemy.eRect[j].x = enemy.x[j]
                    enemy.eRect[j].y = enemy.y[j]
                player.lives -= 1
                if player.lives <= 0:
                    player.lives = 0
                    player.vY = 0
                    player.vX = 0
                    alive = False
                    game_over_text()
                    break

            if alive:    
                enemy.y[i] += enemy.vY[i]
                enemy.eRect[i].x = enemy.x[i]
                enemy.eRect[i].y = enemy.y[i]
                if enemy.y[i] < 0:
                    enemy.vY[i] = enemy.speed
                    enemy.x[i] -= enemy.vX[i]
                elif enemy.y[i] >= 654:
                    enemy.vY[i] = -enemy.speed
                    enemy.x[i] -= enemy.vX[i]
            
            if rocket.rRect.colliderect(enemy.eRect[i]):
                killed = mixer.Sound("Data/sounds/invaderkilled.wav")
                killed.play()
                rocket.rstate = "ready"
                enemy.x[i] = rd.randint(600,1100)
                enemy.y[i] = rd.randint(0,654)
                rocket.rRect.x = -40
                rocket.rRect.y = -40
                score.score += 10
            
            #Player collision with enemy
            if player.pRect.colliderect(enemy.eRect[i]):
                playerHit = mixer.Sound("Data/sounds/playerhit.wav")
                playerHit.play()
                enemy.x[i] = rd.randint(640,1100)
                enemy.y[i] = rd.randint(0,654)
                enemy.eRect[i].x = enemy.x[i]
                enemy.eRect[i].y = enemy.y[i]
                player.lives -= 1
                break
            if player.lives <= 0:
                alive = False
                player.lives = 0
                player.vY = 0
                player.vX = 0
                game_over_text()
            
            if not start_screen:
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


        if not start_screen:    
            SCREEN.blit(player.pImg, (player.x,player.y))
            showScore(score.x, score.y)
            showLives(1120,16)
       
        #Update display when there is a change
        pygame.display.update()

    #Quit the game after closing

if __name__ == "__main__":
    main()