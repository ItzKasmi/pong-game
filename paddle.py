from turtle import Turtle
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        x_cord = self.xcor()
        y_cord = self.ycor()
        if y_cord + 60 > 290:
            pass
        else:
            self.goto(x_cord, y_cord + 15)

    def down(self):
        x_cord = self.xcor()
        y_cord = self.ycor()
        if y_cord - 60 < -280:
            pass
        else:
            self.goto(x_cord, y_cord - 15)
