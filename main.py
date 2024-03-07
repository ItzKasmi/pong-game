from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

STARTING_POSITIONS = [(-350, 0), (350, 0)]

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
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle1 = Paddle(STARTING_POSITIONS[0])
paddle2 = Paddle(STARTING_POSITIONS[1])

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle2.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() < -320 or ball.distance(paddle2) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect out of bounds
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()


screen.exitonclick()
