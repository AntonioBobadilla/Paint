

"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""
import math
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up() #quit the draw
    goto(start.x, start.y) #move the turtle to the first point
    down() #start to draw
    goto(end.x, end.y) #move the turtle to the second point

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y) #begin in the first point
    down()
    begin_fill()

    for count in range(4): #do four lines
        forward(end.x - start.x)
	#move the turtle the size betwen the first and the second point
        left(90) #change the direction of the turtle

    end_fill()

#---in comming ----------------------------------------------------------------------
def circlet(start, end):
    up()
    goto(start.x+((end.x-start.x)/2), start.y+((end.y-start.y)/2)) # start to drawing the circle in the middle of x and y
    down()
    begin_fill() # start to fill with black color
    circle(max( (abs(end.x-start.x)),  abs( (end.y-start.y) ) )/2) # get a radius of 15
    end_fill() # end to fill the figure

def rectangle(start, end):

    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range (2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    end_fill()

def triangle(start, end):

    up()
    goto(start.x,end.y)
    begin_fill()
    down()
    forward(end.y - start.y)
    left(90)
    forward(end.x - start.x)
    left(180-(math.degrees((math.atan((end.y - start.y)/(end.x - start.x))))))
    forward(math.sqrt(((end.y - start.y)**2)+((end.x - start.x)**2)))
    end_fill()
#------------------------------------------------------------------------------------

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y) #Define the first point
    else:
        shape = state['shape']	#Read shape in state at shape
        end = vector(x, y)	#Define the second point
        shape(start, end)	#Call the function x
        state['start'] = None	#Initialize the first point, not the type

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line} #initialize
setup(420, 420, 370, 0) #Size of windows
#	largo, alto, corrdenada x, y


onscreenclick(tap)
"""i think that return interruptions of GI"""
listen()
"""----------------------------------------------------------------------???"""
onkey(undo, 'u')
"""  i think that only keep the states values"""

#Change color del trazo
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')

#Change type de trazo
##call the funtion store  whith shape and the type.
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circlet), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

"""
how the function (store and tap) act into the code. ??????????????????????????????????
"""

"""
-------------------------------------------------------------------------------------
Estaria interesante:
-implementar undo para hacer un ctrl z.
-implementar pensize para cambiar la brocha.
-add the clear

Creo:
-la velocidad con la que grafica varia.
-what is lambda?, what do lambda?
-why in each draw up the pen, cant up it after do the draw?
	...forget this, i'm dum.
	-but this could be on the end, or not?

No tiene nada que ver:
-creo que tron usa distance para ver la colicion, estaria interesante ver como lo
	implementa pero ahora no tengo ganas (22:41).
-
"""
