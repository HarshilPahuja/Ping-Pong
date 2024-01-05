from turtle import Screen
from gamescreen import Main_Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
screen.title("Ping Pong")
screen.setup(width=600,height=600)
screen.bgcolor('black')

main_screen=Main_Screen()
scoreboard=Scoreboard()
main_ball=Ball()
segment1=Paddle()
segment2=Paddle()
segment1.goto(x=260,y=0)
segment2.goto(x=-260,y=0)


screen.listen()
screen.onkey(key='Up',fun=segment1.move_up)
screen.onkey(key='Down',fun=segment1.move_down)
screen.onkey(key='w',fun=segment2.move_up)
screen.onkey(key='s',fun=segment2.move_down)


game_is_on=True

while main_screen.ycor() > -300:
    main_screen.create_centreline()

while game_is_on:
    main_ball.start()

    if main_ball.ycor()>290 or main_ball.ycor()<-290:
        main_ball.wall_bounce()

    if main_ball.distance(segment1) <50 and main_ball.xcor()>250 or main_ball.distance(segment2)<50 and main_ball.xcor()<-250:
        main_ball.paddle_bounce()

    if main_ball.xcor()>290:
        main_ball.missed()
        scoreboard.l_point()

    if main_ball.xcor() < -290:
        main_ball.missed()
        scoreboard.r_point()



screen.exitonclick()