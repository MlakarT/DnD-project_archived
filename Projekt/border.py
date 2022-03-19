import sys
import math
 #grid_x_init is the initial starting value
 #grid_y_init
 #grid_w is the width in x
 #grid_h is the height in y
border = 50
def create_border(X:int, Y:int):
    grid_x_init = X // 4 #ratio is 1/4
    grid_y_init = Y // 12 #maintain 3/4 ratio for grid
    grid_width = X - grid_x_init - border
    grid_h = Y - grid_y_init - border
    return (grid_x_init,grid_y_init,grid_width,grid_h)

