#This is the beginning of the D&D map project. Author: Timotej Mlakar
#This code will be based first on a current map im working on, later to be expanded (like use input) and submitted as school work.
#If i choose to add anything, more at https://github.com/MlakarT/DnD-project
#For any issues or questions please contact me at timo.mlakar@gmail.com or at my university email tm2012@student.uni-lj.si
#The program will use Pygame for drawing purposes

from email.policy import default
import sys
import math
from tkinter import LEFT
from turtle import window_width

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
#l = 200 #temporary
#h = 50 #temporary
#z = 1
#map_seed = 'asfkjg'
light_grey =(211, 211, 211)
red =  (255,0,0)
seed_box = pygame.Rect(50,200,200,40)
seed_text = map_seed

seed_input_color = light_grey

seed_l_box = pygame.Rect(50,300,200,40)
seed_l_text = str(l)
seed_h_box = pygame.Rect(50,400,200,40)
seed_h_text = str(h)
seed_z_box = pygame.Rect(50,500,200,40)
seed_z_text = str(z)

seed_error_message_text = 'Wrong number of characters!'
seed_error_message_color = red
seed_error_message_font = pygame.font.SysFont('calibri',12)

# ---------------------------------------------------------------
#Refresh button -------------------------------------------------
green = (153, 250, 118)
dark_green = (0, 128, 0)
refresh_text = "Refresh"
refresh_font = pygame.font.SysFont('calibri',64)
refresh_button = pygame.Rect(50,(border.refresh_bottom_border(Y)), 220,80)
refresh_color = green
# ---------------------------------------------------------------

grey = (128,128,128)
grid_x_init, grid_y_init, grid_width, grid_height = border.create_border(X,Y)
sq_side = grid_width // l

#Calculate max grid height

h = border.calculate_max_h(grid_y_init,sq_side,grid_height,h)


grid = pygame.Rect(grid_x_init, grid_y_init, l * sq_side, h * sq_side)
print(map)

#----------------------------------------------------------------
#Dungeon prereqs: dev build:

bridge1 = pygame.image.load("Projekt\Assets\Bridge1.jpg")
bridge2 = pygame.image.load("Projekt\Assets\Bridge2.jpg")
platform = pygame.image.load("Projekt\Assets\Platform.jpg")
beginning_platform = pygame.image.load("Projekt\Assets\Beginning_platform.png")
ending_platform = pygame.image.load("Projekt\Assets\Beginning_platform.png")

#bridge1_default_size = bridge1.get_size()
#bridge1_size = bridge1_default_size
default_bridge_size = sq_side, 2 * sq_side
default_platform_size = sq_side * 3, sq_side * 3
default_beginning_platform_size = sq_side * 5, sq_side
bridge1 = pygame.transform.scale(bridge1, default_bridge_size)
bridge2 = pygame.transform.scale(bridge2, default_bridge_size)
platform = pygame.transform.scale(platform, default_platform_size)
beginning_platform = pygame.transform.scale(beginning_platform, default_beginning_platform_size)
ending_platform = pygame.transform.scale(ending_platform, default_beginning_platform_size)
bridge1_rotated = pygame.transform.rotate(bridge1, 90)
bridge2_rotated = pygame.transform.rotate(bridge2, 90)

#starting_l = 0
#starting_h = 1
#step_list = seed.steps(map, starting_l, starting_h)
#print(step_list)
#Infinite loop --------------------------------------------------
state = True
text_active = False
grid_active = False
refresh_active = False
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            window.fill(white)
            X,Y = window.get_size()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #<- Aktivira okna posebej #event.button == 1 preveri, ce je biu levi klik
            text_active = input_box.collidepoint(event.pos)
            grid_active = grid.collidepoint(event.pos)
            seed_active = seed_box.collidepoint(event.pos)
            seed_l_active = seed_l_box.collidepoint(event.pos)
            seed_h_active = seed_h_box.collidepoint(event.pos)
            seed_z_active = seed_z_box.collidepoint(event.pos)
            refresh_active = refresh_button.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN: # <- zazna če tipkas, vsak state posebej
            if text_active:
                if event.key == pygame.K_BACKSPACE: # Check for backspace
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            elif seed_active:
                if event.key == pygame.K_BACKSPACE:
                    seed_text = seed_text[:-1]
                else:
                    seed_text += event.unicode
            elif seed_l_active:
                if event.key == pygame.K_BACKSPACE:
                    seed_l_text = seed_l_text[:-1]
                else:
                    seed_l_text += event.unicode
            elif seed_h_active:
                if event.key == pygame.K_BACKSPACE:
                    seed_h_text = seed_h_text[:-1]
                else:
                    seed_h_text += event.unicode
            elif seed_z_active:
                if event.key == pygame.K_BACKSPACE:
                    seed_z_text = seed_z_text[:-1]
                else:
                    seed_z_text += event.unicode
            
            

#----------------------------------------------------------------
#Code goes here
#----------------------------------------------------------------
    
# Test text box 1 ----------------------------------------------------- 
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

#Seed boxes -----------------------------------------------------
    
    pygame.draw.rect(window, seed_input_color, seed_box)
    if len(seed_text) == 10:
        seed_surface = input_font.render(seed_text ,True, (0,0,0))
        window.blit(seed_surface, (seed_box.x+5, seed_box.y+5))
        seed_box.w = max (200, seed_surface.get_width()+10)
    else:
        seed_surface = seed_error_message_font.render(seed_error_message_text, True, (0,0,0))
        window.blit(seed_surface,(seed_box.x,seed_box.y+50))
    
    pygame.draw.rect(window, seed_input_color,seed_l_box)
    seed_l_surface = input_font.render(seed_l_text, True, (0,0,0))
    window.blit(seed_l_surface, (seed_l_box.x+5,seed_l_box.y+5))
    seed_l_box.w = max (200, seed_l_surface.get_width()+10)
    
    pygame.draw.rect(window, seed_input_color,seed_h_box)
    seed_h_surface = input_font.render(seed_h_text, True, (0,0,0))
    window.blit(seed_h_surface, (seed_h_box.x+5,seed_h_box.y+5))
    seed_h_box.w = max (200, seed_h_surface.get_width()+10)

    pygame.draw.rect(window, seed_input_color,seed_z_box)
    seed_z_surface = input_font.render(seed_z_text, True, (0,0,0))
    window.blit(seed_z_surface, (seed_z_box.x+5,seed_z_box.y+5))
    seed_z_box.w = max (200, seed_z_surface.get_width()+10)

#----------------------------------------------------------------
#Refresh button -------------------------------------------------
    pygame.draw.rect(window,refresh_color, refresh_button)
    refresh_surface = refresh_font.render(refresh_text, True, (0,0,0))
    window.blit(refresh_surface, (refresh_button.x+10,refresh_button.y+10))   

    if refresh_active:
        refresh_color = dark_green
        seed_text = seed_l_text.zfill(2) + seed_h_text.zfill(2) + seed_z_text + str(unique_identifier)
        print(seed_text)
        l, h, z, unused_identifier = seed.read(seed_text) #unused identifier sa napise samo v prazno, zato da ostane isti identifier
        #step_list = seed.steps(seed.read(seed_text), starting_l, starting_h)
        print(seed.read(seed_text))
        refresh_active = False

#Grid -----------------------------------------------------------
    if len(seed_text) == 10:    
        sq_side = grid_width // l
        h = border.calculate_max_h(grid_y_init,sq_side,grid_height,h) #<- ta stvar prepreci da bi se izrisala 1x1 mreza

#Calculating image size -----------------------------------------
        default_bridge_size = sq_side, 2 * sq_side
        default_platform_size = sq_side * 3, sq_side * 3
        default_beginning_platform_size = sq_side * 5, sq_side
        scaled_bridge1 = pygame.transform.scale(bridge1, default_bridge_size)
        scaled_bridge2 = pygame.transform.scale(bridge2, default_bridge_size)
        scaled_platform = pygame.transform.scale(platform, default_platform_size)
        scaled_beginning_platform = pygame.transform.scale(beginning_platform, default_beginning_platform_size)
        beginning_platform_rotated = pygame.transform.rotate(scaled_beginning_platform, 90)
        bridge1_rotated = pygame.transform.rotate(scaled_bridge1, 90)
        bridge2_rotated = pygame.transform.rotate(scaled_bridge2, 90)
        starting_l = 0 * sq_side
        starting_h = 1 * sq_side
#---------------------------------------------------------------
#Temporary draw window -----------------------------------------
        
        #for i in step_list:
        #    if i[0] == 0: #bridge 1
        #        if i[2] == 0 or i[2] == 180:
        #            window.blit(bridge1_rotated, (grid_x_init + i[1][0] * sq_side, grid_y_init + i[1][1] * sq_side))
        #        else:
        #            window.blit(scaled_bridge1, (grid_x_init + i[1][0] * sq_side, grid_y_init + i[1][1] * sq_side))
        #    elif i[0] == 1: # bridge 2
        #        if i[2] == 0 or i[2] == 180:
        #           window.blit(bridge2_rotated, (grid_x_init + i[1][0] * sq_side, grid_y_init + i[1][1] * sq_side))
        #        else:
        #             window.blit(scaled_bridge2, (grid_x_init + i[1][0] * sq_side, grid_y_init + i[1][1] * sq_side))
        #    elif i[0] == 2: #platform
        #        window.blit(scaled_platform, (grid_x_init + i[1][0] * sq_side, grid_y_init + i[1][1] * sq_side))
            #elif i[1][0] > grid_width or i[1][1] > grid_height:
            #    break
        # This code should suffice for drawing, just needs more.... pizzazz
        for i in range(0,(h-1) // 2):
            window.blit(scaled_bridge1, (grid_x_init + (l // 2 - 1) * sq_side, grid_y_init + sq_side + 2 * i * sq_side))
        #window.blit(scaled_platform, (grid_x_init + (l // 2 - 2) * sq_side, h // 2 * sq_side))
        window.blit(scaled_beginning_platform, (grid_x_init + (l// 2 - 3) * sq_side, grid_y_init))
        window.blit(scaled_beginning_platform, (grid_x_init + (l // 2 - 3) * sq_side, grid_y_init + (h-1) * sq_side))
        #window.blit(scaled_bridge1, (grid_x_init, grid_y_init))
        #window.blit(scaled_bridge2, (grid_x_init + 3 * sq_side, grid_y_init))
        #window.blit(scaled_platform, (grid_x_init + 6 * sq_side, grid_y_init))

#---------------------------------------------------------------
        for i in range(l):
            for j in range(h): #range gre do h - 1, v tem seznamu ni h-ja
                pygame.draw.rect(window,grey,(grid_x_init + i * sq_side,grid_y_init + j * sq_side, sq_side, sq_side),1)
        pygame.draw.rect(window,black,(grid_x_init, grid_y_init, l * sq_side, h * sq_side),5) # <----this is fix

#This window is the grid surface, will be used for drawing later-
    #if grid_active: #this thing is gonna draw my grid
        #pygame.draw.rect(window,grey,grid) # <-- tega ne rabim

    
#Window updates -------------------------------------------------
    pygame.display.update()
    clock.tick(30)

#Quit Pygame ----------------------------------------------------
pygame.quit()
quit()