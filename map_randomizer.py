#This is the beginning of the D&D map project. Author: Timotej Mlakar
#This code will be based first on a current map im working on, later to be expanded (like use input) and submitted as school work.
#If i choose to add anything, more at https://github.com/MlakarT/DnD-project
#For any issues or questions please contact me at timo.mlakar@gmail.com or at my university email tm2012@student.uni-lj.si
#The program will use Pygame for drawing purposes

import sys
import math

import pygame
from pygame.locals import *
#import grid <------------ unused import, changed my mind mid way
import border
import seed

#Initiate Pygame ------------------------------------------------
pygame.init()

#Pygame clock ---------------------------------------------------
clock = pygame.time.Clock()

#Window prereqs -------------------------------------------------
X,Y = 1600,900 # <---- Primary window size
black = (0,0,0)
white = (255,255,255)
window = pygame.display.set_mode((X,Y),pygame.RESIZABLE)
window.fill(white)
pygame.display.set_caption("Map Randomizer")
pygame.display.flip()

#Input prereqs --------------------------------------------------
input_font = pygame.font.SysFont('arial',32)
user_text = ''
input_box = pygame.Rect(50,100,200,40)
color_active = pygame.Color('lightskyblue3')
color_passive = (192, 192, 192)

input_box_color = color_passive 

#Grid prereqs ---------------------------------------------------
#A seedy place --------------------------------------------------
map_seed = seed.generate()
map = seed.read(map_seed)
l, h , z , unique_identifier = map
seed_box = pygame.Rect(50,200,200,40)
seed_text = map_seed

# ---------------------------------------------------------------

grey = (128,128,128)
grid_x_init, grid_y_init, grid_width, grid_height = border.create_border(X,Y)
#l = 40 #temporary, will replace later with user_input_length
#h = 30 #temporary, will replace later with user_input_height
sq_side = grid_width // l
#if grid_y_init + h * sq_side + border.border > Y: # <---- Ta stvar 
#    h = 
    #while grid_y_init + h * sq_side + border.border > Y:
    #    h -=1

#Calculate max grid height

for i in range(h+1):
    if grid_y_init + (i) * sq_side > grid_height:
        h = i - 1
        break
    else:
        continue

grid = pygame.Rect(grid_x_init, grid_y_init, l * sq_side, (h+1) * sq_side)
print(map)

#Infinite loop --------------------------------------------------
state = True
text_active = False
grid_active = False
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            window.fill(white)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                text_active = True
            else:
                text_active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE: # Check for backspace
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if grid.collidepoint(event.pos):
                grid_active = True
            else: 
                grid_active = False

#----------------------------------------------------------------
#Code goes here
#----------------------------------------------------------------
    
#Text box 1 ----------------------------------------------------- 
    if text_active:
        input_box_color = color_active #determines the input box color in both states
    else:
        input_box_color = color_passive#determines the input box color in both states
    window.fill(white)
    pygame.draw.rect(window, input_box_color,input_box)
    text_surface = input_font.render(user_text, True, (0,0,0))
    window.blit(text_surface, (input_box.x+5, input_box.y+5))
    input_box.w = max(200, text_surface.get_width()+10)

#----------------------------------------------------------------

#Seed box -------------------------------------------------------
    pygame.draw.rect(window, input_box_color, seed_box)
    seed_surface = input_font.render(seed_text ,True, (0,0,0))
    window.blit(seed_surface, (seed_box.x+5, seed_box.y+5))
    seed_box.w = max (200, seed_surface.get_width()+10)

#----------------------------------------------------------------
    
#Grid -----------------------------------------------------------
    for i in range(l):
        for j in range(h): #range gre do h - 1, v tem seznamu ni h-ja
            pygame.draw.rect(window,grey,(grid_x_init + i * sq_side,grid_y_init + j * sq_side, sq_side, sq_side),1)
        #if h * sq_side > grid_height:
        #    pygame.draw.rect(window,black,(grid_x_init,grid_y_init,grid_width,grid_height),5)
        #else:
    pygame.draw.rect(window,black,(grid_x_init, grid_y_init, l * sq_side, h * sq_side),5) # <----this is fix

#This window is the grid surface, will be used for drawing later-
    if grid_active == True: #this thing is gonna draw my grid
        pygame.draw.rect(window,grey,grid)
    

#Window updates -------------------------------------------------
    pygame.display.update()
    clock.tick(1)

#Quit Pygame ----------------------------------------------------
pygame.quit()
quit()