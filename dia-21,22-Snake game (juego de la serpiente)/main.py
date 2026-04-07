from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
from turtle import Screen
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Steve´s snake game")
screen.tracer(0)
screen.listen()

#Variables
score = 0


my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()

#Controles
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    my_scoreboard.puntuar(score)

    #Detect colission
    if my_snake.segments[0].distance(my_food) < 15:
        my_snake.grow()
        my_food.appear()
        score += 1
        my_scoreboard.limpiar()

    #Perder por chocar con la pared
    if my_snake.segments[0].xcor() >= 300 or my_snake.segments[0].ycor() >= 300 or my_snake.segments[0].xcor() <= -300 or my_snake.segments[0].ycor() <= -300:
        my_scoreboard.perder(score)
        game_is_on = False

    #Detectar si chocamos con nuestra cola
    for segment in my_snake.segments[1:]:
        if my_snake.segments[0].distance(segment) < 10:
            my_scoreboard.perder(score)
            game_is_on = False




screen.exitonclick()
