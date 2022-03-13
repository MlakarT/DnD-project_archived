#This is the beginning of the D&D map project. Author: Timotej Mlakar
#This code will be based first on a current map im working on, later to be expanded (like use input) and submitted as school work.
#If i choose to add anything, more at https://github.com/MlakarT/DnD-project
#For any issues or questions please contact me at timo.mlakar@gmail.com or at my university email tm2012@student.uni-lj.si
#The program will use Pygame for drawing purposes

import sys
import math
from tkinter import Grid

import pygame
import grid
import border

#Initiate Pygame ------------------------------------------------
pygame.init()

#Pygame clock ---------------------------------------------------
clock = pygame.time.Clock()

#Window prereqs -------------------------------------------------
X,Y = 1600,900 # <---- Primary window size
white = (255,255,255)
window = pygame.display.set_mode((X,Y),pygame.RESIZABLE)
window.fill(white)
pygame.display.set_caption("Map Randomizer")
pygame.display.flip()

#Infinite loop --------------------------------------------------
state = True
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            window.fill(white)

#----------------------------------------------------------------
#Code goes here
#----------------------------------------------------------------
    #X_init, Y_init = border.create_border(X,Y)
    

#Window updates -------------------------------------------------
    pygame.display.update()
    clock.tick(30)

#Quit Pygame ----------------------------------------------------
pygame.quit()
quit()