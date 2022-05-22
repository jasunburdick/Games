from operator import pos
import random
from os import system, name
from time import sleep
from pynput.keyboard import Key, Listener

size = 30                               # Variables
width = size*3
map = []
position = [0, size]
player = [0,size]

for i in range(size):                   # Build empty map
    map.append([" "]*width)

#map[position[0]][position[1]] = '0'     # Draw starting 

def clear():
    if name == 'nt':                    # for windows
        _ = system('cls')
    
    else:                               # for mac and linux
        _ = system('clear')

keys = {Key.left: (1,-1), Key.right: (1,1), Key.up: (0,-1), Key.down: (0,1)}

def keyDirections(dir):
    player[keys[dir][0]] += keys[dir][1]
    if map[player[0]][player[1]] == '0' or map[player[0]][player[1]] == '^':
        map[player[0]][player[1]] = '^'
    else:
        player[keys[dir][0]] -= keys[dir][1]
    
def actions(key):                          # Event Handler moves player
    if key == Key.left:
        keyDirections(key)
    if key == Key.right:
        keyDirections(key)
    if key == Key.up:
        keyDirections(key)
    if key == Key.down:
        keyDirections(key)
    # terminate the loop 
    if key == Key.delete: 
        print("Done")
        return False
    clear()
    printBoard(map)

def printBoard(map):
    for i in range(size):
        mapString = "".join(map[i])
        print(mapString)

def boundary(position):
    if position[0] > size-1:
        position[0] = size-1
    if position[1] > width-1:
        position[1] = width-1  
    return position

def room(map, position):
    y = position[0]
    x = position[1]
    for i in range(5):
        for j in range(5):
            position[0] = y + i
            position[1] = x + j
            position = boundary(position)
            map[position[0]][position[1]] = '0'
    start = [y,x]
    return map, position, start

def hallway(map, position):
    for i in range(10):
        position[1] += 1
        position = boundary(position)
        map[position[0]][position[1]] = '0'
    return map, position

def navigateDown(map, position):
    while position[0] < size-1:
        y = random.randint(0,1)
        z = random.randint(0,5)
        if y == 1:
            x = 0
        else:
            x = random.choice([-1,1])
        position[0] += y
        position[1] += x
        if y == 0 and z == 0:
            map, position, start = room(map, position)         ### Room maker
            position[0] += 1
            position = boundary(position)
            map[position[0]][position[1]] = '0'
            map, position = hallway(map, position)
            #map, position = navigateDown(map, position)       ### multipath
        position = boundary(position)
        map[position[0]][position[1]] = '0'
    return map, position

def main(map, position):
    position[0] += 1
    map[position[0]][position[1]] = '0'
    map, position = navigateDown(map, position)
    #sleep(2)
    # Collect all event until released
    with Listener(on_press = actions) as listener:
        listener.join()
    x = input("")       # Keep code open

if __name__ == "__main__":
    main(map, position)