import sys
import math 

import pygame
from pygame.locals import *
    #print(sys.path)
# Prerequisite definitions --------------------------------------------------
def grid():
#----------------------------------------------------------------------------
#Initiate Pygame
    pygame.init()

#Clock goes here if its necessary
    clock = pygame.time.Clock()
#Defs -----------------------------------------------------------------------
    black = (0,0,0)
    white = (255,255,255)
    grey = (128,128,128)
    X = 1200 #<- Te dve se stpreminjata #ce nastimam 1880 1000 se umes med kvadratki pojaujo spaci :/
    Y = 900 #<- Te dve se stpreminjata
    Z = 0
    l = 40 #in game units
    h = 30 #in game units

#window setup
    window = pygame.display.set_mode((X, Y))# """pygame.RESIZABLE"""
    window.fill(white) # <- tuki se lohk importa background image
    pygame.display.set_caption("Grid")
    #background_image = pygame.image.load('default_background.jpg')
    #window.blit(background_image,(0,0))
    #pygame.display.flip()

#While loop poganja konstantno window -------------------------------------------

    state = True
    while state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False #if the user wants to close the window, close the window

#---------------------------------------------------------------------------------
#Here goes the code --------------------------------------------------------------

        sq_side = X // l
        for i in range(l):
            for j in range(h):
                pygame.draw.rect(window,grey,(i * sq_side,j * sq_side, sq_side, sq_side),1)
        if h * sq_side > Y:
            pygame.draw.rect(window,black,(0,0,X,Y),5)
        else:
            pygame.draw.rect(window,black,(0,0,X,h * sq_side),5)
       
#Pygame window updates go here ---------------------------------------------------    
        pygame.display.update()
        clock.tick(10)
#---------------------------------------------------------------------------------

#Quit Pygame
    pygame.quit()
    quit()

