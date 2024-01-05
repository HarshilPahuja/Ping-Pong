from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed('fastest')

        self.xmove=1.5
        self.ymove=1.5

    def start(self):
        new_x=self.xcor()+ self.xmove
        new_y=self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.ymove *= -1
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def paddle_bounce(self):
        self.xmove *= -1
        self.ymove *= -1
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def missed(self):
        self.setposition(0,0)
        time.sleep(0.5)
        self.paddle_bounce()









