from turtle import Turtle

#Variables
ALIGNMENT = "center"
FONT = ("¨Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,250)


    def puntuar(self, puntos):
        self.write(f"Puntuacion = {puntos}", False ,ALIGNMENT, FONT)

    def limpiar(self):
        self.clear()

    def perder(self, puntos):
        self.goto(0, 0)
        self.write(f"PERDISTE!", False ,ALIGNMENT, FONT)
