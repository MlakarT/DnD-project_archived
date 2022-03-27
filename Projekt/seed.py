# Code for anything to do with the seed, seed generating, seed reading and controll


import random as rd
from tracemalloc import start

# Generate seed
def generate():
    l = str(rd.randint(3,50))
    l = l.zfill(2)
    h = str(rd.randint(2,50))
    h = h.zfill(2)
    z = str(rd.randint(1,5))
    unique_identifier = str(rd.randint(0,99999))
    unique_identifier = unique_identifier.zfill(5)
    return l + h + z + unique_identifier

    #return str(rd.randint(0,50)) + str(rd.randint(0,50)) + str(rd.randint(0,5)) + str(rd.randint(0,99999))

def read(strg):
    l = int(strg[:2])
    h = int(strg[2:4])
    z = int(strg[4])
    unique_identifier = int(strg[5:])
    return (l,h,z, unique_identifier)
    
basic_map = 0,0

def steps(map:tuple , starting_l=0, starting_h=1,):
    map_length = sum(int(i) for i in str(map[3])) #<----- calculate map length based on unique_identifier
    list_of_steps = []
    i = 0
    j = 0
    while i <= map_length:
        if j % 3 == 0:
            list_of_steps.append([j % 3, (starting_l + i,starting_h), 0])
            i += 2
            j += 1
        elif j % 3 == 1:
            list_of_steps.append([j % 3, (starting_l + i,starting_h), 0])
            i += 2
            j += 1
        elif j % 3 == 2:
            list_of_steps.append([j % 3, (starting_l + i,starting_h - 1), 0]) 
            i += 3
            j += 1
    return list_of_steps

def basic_steps(map:tuple ,sq_side:int, starting_x=0, starting_y=0,):
    map_length = sum(int(i) for i in str(map[3]))
    list_of_steps = []
    i = 0
    while i <= map_length:
        list_of_steps.append([i % 3, (starting_x + 2 * i * sq_side, starting_y), 0])
        i += 1
    return list_of_steps