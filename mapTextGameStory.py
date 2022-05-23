from ast import Try
from operator import pos
from platform import java_ver
import random
from os import system, name
from time import sleep
from tkinter import N
from pynput.keyboard import Key, Listener

size = 30                               # Variables
width = size*3
playerName = ""
map = []
position = [0, size]
player = [0,size]

for i in range(size):                   # Build empty map
    map.append([[" ",0].copy()]*width)

def clear():
    if name == 'nt':                    # for windows
        _ = system('cls')
    else:                               # for mac and linux
        _ = system('clearerer')

keys = {Key.left: (1,-1), Key.right: (1,1), Key.up: (0,-1), Key.down: (0,1)}

def keyDirections(dir):
    global player
    player[keys[dir][0]] += keys[dir][1]
    player = boundary(player)
    if map[player[0]][player[1]][0] == '0' or map[player[0]][player[1]][0] == '^':
        map[player[0]][player[1]] = ['^',0]
    else:
        player[keys[dir][0]] -= keys[dir][1]
    for i in range(-1,2):
        for j in range(-1,2):
            try:
                map[player[0]+i][player[1]+j][1] = 1
            except:
                pass

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
        mapString = ""
        for j in range(len(map[i])):
            if map[i][j][1] == 1:           
                mapString += map[i][j][0]
            else:
                mapString += " "

        #mapString = "".join(map[i][0])         # Old map design
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
            map[position[0]][position[1]] = ['0',0]
    start = [y,x]
    return map, position, start

def hallway(map, position):
    for i in range(10):
        position[1] += 1
        position = boundary(position)
        map[position[0]][position[1]] = ['0',0]
    return map, position

def makeMap(map, position):
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
            map[position[0]][position[1]] = ['0',0]
            if x < 1:
                map, position = hallway(map, position)
            #map, position = makeMap(map, position)       ### multipath
        position = boundary(position)
        map[position[0]][position[1]] = ['0',0]
    return map, position

def story():
    script = {1: "*** Once upon a time, while wandering the world.  Our hero " + playerName + " came upon a hole of questionable purpose. ",
        2: "Not having anything else going on that day, you step down in the hole and start to look around. ",
        3: "As the light fades from above, you turn your headlamp on and notice the battery not fully charged. ",
        4: "What do you do next.  Get out and go find some batteries or keep going. ",
        5: "You can be seen on the map as ^. Use the arrow keys to start exploring, delete key quits. "}
    for i in range(1,5):
        print(script[i])
    
    for i in range(2):
        choice = input("Batteries or Explore: ")
        if choice.lower() == "batteries":
            print("You return home and never find the hole again.\n Game over. ")
            return "end"
        elif choice.lower() == "e":
            print(script[5])
            break
        else:
            continue

def main(map, position):
    global playerName     
    #clear()  
    playerName = input("*** Welcome to depth. ***\n  The not so deep game. ***\n What is your name? ")      
    navigate = story()
    if navigate == "end":
        choice = input("Game over... Enter R to restart.  --This doesn't work yet--  ")       # Keep code open
        if choice.lower() == "r":
            main()
        else:
            return
    
    position[0] += 1
    map[position[0]][position[1]] = '0'
    map, position = makeMap(map, position)
    #sleep(2)
    # Collect all event until released
    with Listener(on_press = actions) as listener:
        listener.join()
    x = input("Game over... Enter R to restart.  --This doesn't work yet--  ")       # Keep code open

if __name__ == "__main__":
    main(map, position)

    
