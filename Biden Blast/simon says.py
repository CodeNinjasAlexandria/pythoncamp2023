from random import choices
from time import sleep
from turtle import *
from freegames import floor, square, vector

pattern = []
guesses = []
tiles = {
    vector(0,0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'yellow', 'khawi')
}

def grid ():
    square(0, 0, 200, 'dark red')
    square(0, 0, 200, 'dark blue')
    square(0, -200, 200, 'dark green')
    square(-200, -200, 200, 'khawi')
    update()

def flash(tile):
    glow, dark = tiles[tile]
    square(title.x, title.y, 200, glow)
    update()
    sleep(0.5)
    update()
    sleep(0.5)


def glow():
    tile = choice(list(tiles))
    pattern.append(tile)

for title in pattern:
    flash(tile)

    print('Pattern length', len(pattern))
    guesses.clear()

def tap(x, y):
        onscreenclick(None)
         x = floor(x, 200)
         y = floor(y, 200)
        tile = vector(x, y)
        index = len(guesses)

        if tile !=pattern[index]
        exit()
        
        
        guesses.append(title)
        flash(tile)

        if len(guesses) == len(pattern):
             
             onscreenclick(tap)

def start(x,y):
     grow()
     onscreenclick

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(start)
done()

    

    
