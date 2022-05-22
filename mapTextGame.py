'''
Make a text based world
'''
from math import ceil
import os

map = []
size = 9                    # works for odd numbers
mapAppend = ["aaa"]*size
playerPos = (0,0)

for i in range(size):
    map.append(mapAppend)

roomSize = size
ceiling = "# " * roomSize
ceilingDoor = "# "*(roomSize//2) + "  "*(1) + "# "*(roomSize//2)
def walls(side):
    if side == "l":
        l = "  "
        r = "#"
    elif side == "r":
        l = "# "
        r = " "
    else:
        l = "# "
        r = "#"
    for i in range(roomSize//2-1):
        print("# " + "  "*(roomSize-2) + "#")
    for i in range(1):
        print(l + "  "*(roomSize-2) + r)
    for i in range(roomSize//2-1):
        print("# " + "  "*(roomSize-2) + "#")

def roomType(type):
    if type[0] == "d":
        print(ceilingDoor)
    else:
        print(ceiling)
    walls(type[1])
    if type[2] == "d":
        print(ceilingDoor)
    else:
        print(ceiling)
def clear_console():
    os.system('cls')

roomType("dra")             #d(lrb)d
x = input("")
clear_console()
roomType("dla")
x = input("")
