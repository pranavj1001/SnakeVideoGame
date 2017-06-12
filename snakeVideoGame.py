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