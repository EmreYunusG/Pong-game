from turtle import Turtle



class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.position=position
 
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Adjust the size of the paddle
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(),self.ycor()+20)
    def down(self):
        self.goto(self.xcor(),self.ycor()-20)
