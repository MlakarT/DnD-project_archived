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
    grid_heigth = Y - grid_y_init - border
    return (grid_x_init,grid_y_init,grid_width,grid_heigth)

def refresh_bottom_border(Y:int):
    bottom_border = 50
    return  0.9 * Y - bottom_border

def calculate_max_h(grid_y_init, sq_side, grid_height,h):
    for i in range(h+1):
        if grid_y_init + (i) * sq_side > grid_height:
            h = i - 1
            break
        else:
            continue
    return h

