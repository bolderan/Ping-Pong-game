import turtle as T
import time
import random
from day22_4 import Scoreboard
from day22_2 import Paddel
from day22_3 import Ball
import time
screen = T.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_paddel = Paddel((350, 0))
l_paddel = Paddel((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddel.go_up, "Up")
screen.onkey(r_paddel.go_down, "Down")
screen.onkey(l_paddel.go_up, "w")
screen.onkey(l_paddel.go_down, "s")


game_on = True
while game_on:
    
    time.sleep(ball.move_speed) 
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with paddel
    if (ball.distance(r_paddel) < 50 and ball.xcor() > 320) or (ball.distance(l_paddel) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        
    # detect that ball is out of box 
    if ball.xcor() > 380 :
        ball.reset_pos()
        score.l_point()


    if ball.xcor() < -380 :
        ball.reset_pos()
        score.r_point()



screen.exitonclick()
