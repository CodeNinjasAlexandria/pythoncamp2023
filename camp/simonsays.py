from random import choice
from time import sleep
from turtle import *
from freegames import floor, square, vector
    
pattern = []
guesses = []
tiles = {
    vector(0,0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0):('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki')
    }

def grid():
    print('grid inititated')
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    update()

def flash(tile):
    print('flash initiated')
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    update()
    sleep(0.5)
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(0.5)

def grow():
    print('grow initiatied')
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash(tile)
    
    print('pattern length:', len(pattern))
    guesses.clear()

def tap(x, y):
    print('tap initiated')
    onscreenclick(None)
    print(f'Raw >>> x: {x} - y: {y}')
    x = floor(x, 200)
    y = floor(y, 200)
    print(f'Floored >>> x: {x} - y: {y}')
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        exit()

    guesses.append(tiles)
    flash(tile)

    if len(guesses) == len(pattern):
        grow()
   
    onscreenclick(tap)

def start(x, y):
     grow()
     onscreenclick(tap)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(start)
done()