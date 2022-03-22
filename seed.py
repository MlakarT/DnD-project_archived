# Code for anything to do with the seed, seed generating, seed reading and controll

import random as rd

# Generate seed
def generate():
    l = str(rd.randint(2,50))
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