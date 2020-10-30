"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

#inicializa las coordenadas
food = vector(0, 0)
snake = [vector(10, 0)]
#inicializa el movimiento de la serpiente
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0) #window size and coordinates
hideturtle()
tracer(False) #quit delay in the game drawing
listen() #return keyboard interruptions
#change directions
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
#Add AWSD
#Rigth
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(10, 0), 'D')
#Left
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(-10, 0), 'A')
#Up
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, 10), 'W')
#Down
onkey(lambda: change(0, -10), 's')
onkey(lambda: change(0, -10), 'S')
move()
done()
