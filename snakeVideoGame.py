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