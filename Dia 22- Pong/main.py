from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time
screen = Screen()

#Variables globales
continue_game = True
ball_speed = 0.1

#Configuraciones de la pantalla
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong de steve")
screen.listen()
screen.tracer(0)

#Crear objetos
first_paddle = Paddle(350,0)
second_paddle = Paddle(-350, 0)
my_ball = Ball()
my_scoreboard = Scoreboard()

#Controles
#Jugador 1
screen.onkey(first_paddle.move_up, "Up")
screen.onkey(first_paddle.move_down, "Down")
#Jugador 2
screen.onkey(second_paddle.move_up, "w")
screen.onkey(second_paddle.move_down, "s")

while continue_game:
    time.sleep(ball_speed)
    screen.update()
    my_ball.move()
    my_ball.detect_wall()
    my_ball.detect_paddle(second_paddle)
    my_ball.detect_paddle(first_paddle)
    if my_ball.xcor() > 380:
        my_ball.reset_position()
        my_scoreboard.player_2_point()
        ball_speed -= 0.01

    if my_ball.xcor() < -380:
        my_ball.reset_position()
        my_scoreboard.player_1_point()
        ball_speed -= 0.01



screen.exitonclick()
