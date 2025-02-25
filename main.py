import keyboard
from queue import Queue
import time
import random
import os

map = []
size = 16
snake = Queue(maxsize=size*size)
x = 0
y = 0 
Direction = 0
playing = True
L=0

def Error():
    global map, x, y, size, snake, playing, Direction, L
    playing=False
    print('ERROR')

def OutMap():
    global map, x, y, size, snake, playing, Direction
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(size):
        out = ''
        for j in range(size):
            if [i, j] in list(snake.queue):
                out = out + '@ '
            else:
                out = out + map[i][j]
        print (out)
    print('Score: ', L)
    
def init():
    global map, x, y, size, snake, playing, Direction, L
    for i in range(size):
        map.append([])
        for j in range(size):
            if (i == 0 or i == size-1 or j == 0 or j == size-1):
                map[i].append('$ ')
            else:
                map[i].append('. ')
    map[size//2][size//2] = '@ '
    x = size // 2
    y = size // 2
    while not snake.empty():
        snake.get()
    snake.put([x,y])
    food()


def goup():
    global map, x, y, size, snake, playing, Direction, L
    cell=[]
    if map[x-1][y]=='. ':
        snake.put([x-1,y])
        cell=snake.get() 
        map[x-1][y]='@ '
        map[cell[0]][cell[1]] = '. '
        x=x-1
    elif map[x-1][y]=='$ ' :
        playing=False
    elif map[x-1][y]=='O ':
        snake.put([x-1,y])
        map[x-1][y]='@ '
        x=x-1
        food()
    else:
        Error()
    Direction = 0


def goright():
    global map, x, y, size, snake, playing, Direction, L
    if map[x][y+1]=='. ':
        snake.put([x,y+1])
        cell=snake.get() 
        map[x][y+1]='@ '
        map[cell[0]][cell[1]] = '. '
        y=y+1
    elif map[x][y+1]=='$ ' :
        playing=False
    elif map[x][y+1]=='O ':
        snake.put([x,y+1])
        map[x][y+1]='@ '
        y=y+1
        food()
    else:
        Error()
    Direction = 1


def goleft():
    global map, x, y, size, snake, playing, Direction, L
    if map[x][y-1]=='. ':
        snake.put([x,y-1])
        cell=snake.get() 
        map[x][y-1]='@ '
        map[cell[0]][cell[1]] = '. '
        y=y-1
    elif map[x][y-1]=='$ ' :
        playing=False
    elif map[x][y-1]=='O ':
        snake.put([x,y-1])
        map[x][y-1]='@ '
        y=y-1
        food()
    else:
        Error()
    Direction = 3


def godown():
    global map, x, y, size, snake, playing, Direction, L
    if map[x+1][y]=='. ':
        snake.put([x+1,y])
        cell=snake.get() 
        map[x+1][y]='@ '
        map[cell[0]][cell[1]] = '. '
        x=x+1
    elif (map[x+1][y]=='$ ' or map[x+1][y]=='@ ') :
        playing=False
    elif map[x+1][y]=='O ':
        snake.put([x+1,y])
        map[x+1][y]='@ '
        x=x+1
        food()
    else:
        Error()
    Direction = 2



def go():
    global map, x, y, size, snake, playing, Direction, L
    match Direction :
        case 0:
            goup()
        case 1:
            goright()
        case 2:
            godown()
        case 3:
            goleft()

def food():
    global map, x, y, size, snake, playing, Direction, L
    L=L+1
    RandR = random.randint(0, size-1)
    RandC = random.randint(0, size-1)
    cell=[RandR, RandC]
    cpt=1

    while map[cell[0]][cell[1]] != '. ' and cpt<100:
        RandR = random.randint(0, size-1)
        RandC = random.randint(0, size-1)
        cell=[RandR, RandC]
        cpt=cpt+1
    map[cell[0]][cell[1]]='O '


def main():
    global map, x, y, size, snake, playing, Direction, L
    print('start game??')
    input("Press Enter to continue...")
    init()
    cpt= 0
    choice = None
    while playing:
        if keyboard.is_pressed("up"):
                choice=0
        elif keyboard.is_pressed("left"):
            choice=3
        if keyboard.is_pressed("right"):
            choice=1
        elif keyboard.is_pressed("down"):
            choice=2
        if cpt > 1:
            if choice==0:
                goup()
            elif choice==3:
                goleft()
            if choice==1:
                goright()
            elif choice==2:
                godown()
            else:
                go()
            cpt=0
        OutMap()
        cpt=cpt+1
        time.sleep(0.1)
main()