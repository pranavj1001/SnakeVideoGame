#Simple Snake Game like the one from Nokia Phones
#Built using Python Language and PyGame Package

import pygame, sys, random, time

checkErrors = pygame.init() #should be (6,0) 6 means that it completed six successful tasks and 0 means that there were zero errors

#if errors are found then exit else continue
if checkErrors[1] > 0:
    print("Errors were found, please fix it, exiting.....")
    sys.exit(-1)
else:
    print("Game was successfully initialized")
    
#Board to play
heightWidthTuple = (720, 460)
playBoard = pygame.display.set_mode(heightWidthTuple)

#set the window header
pygame.display.set_caption("Snake Video Game")

#Colors: (R, G, B) values are from 0 to 255 
red = pygame.Color(255, 0, 0) # gameOver
green = pygame.Color(0, 255, 0) # snake
blue = pygame.Color(0, 0, 255) # use not defined
black = pygame.Color(0, 0, 0) # score
white = pygame.Color(255, 255, 255) # background
brown = pygame.Color(165, 42, 42) # food

#Game Variables
fpsController = pygame.time.Clock() # FPS controller

snakePosition = [360, 230]
snakeBody = [[360, 230], [350, 230], [340, 230]]

foodPosition = [random.randrange(1,72)*10, random.randrange(1,46)*10]
foodSpawn = True

direction = "RIGHT"
changeTo = direction

# Game Over Function
def gameOver():
    font = pygame.font.SysFont('monaco', 72)
    gameOverText = font.render('Game Over!', True, red)
    gameOverRect = gameOverText.get_rect()
    gameOverRect.midtop = (360, 30)
    playBoard.blit(gameOverText, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()
    
#Main logic
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT)) # create an event to quit the game