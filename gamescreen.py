from turtle import Turtle
class  Main_Screen(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setposition(x=0, y=300)
        self.setheading(270)


    def create_centreline(self):
        self.forward(10)
        self.penup()
        self.forward(10)
        self.pendown()



