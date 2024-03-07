from turtle import Screen
from paddle import Paddle
import time

'''
Breakdown the problem -

1. Need to create a screen and background for our game
2. Need to create a turtle object to act as a paddle
    a. create a second turtle object to act as the second paddle but bound to separate keys (W,S/Up,Down)
3. Create a ball object
    a. Make it constantly move in a direction
    b. Change direction and angle based on impact
        1. swap direction 180 plus or less depending on height of paddle
        2. Also change direction if it hits the ceiling or floor
4. Create the 'map' and scoreboard
    a. Make a center line that decides which side gets the point
    b. Create a ceiling and floor for ball to bounce
    c. Create out of bound walls on left and right
'''

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

STARTING_POSITIONS = [(-500, 0), (500, 0)]

paddle1 = Paddle(STARTING_POSITIONS[0])
paddle2 = Paddle(STARTING_POSITIONS[1])

screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle2.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.075)

screen.exitonclick()
