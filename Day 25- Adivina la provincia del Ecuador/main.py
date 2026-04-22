import turtle
from xxsubtype import bench

import pandas

screen = turtle.Screen()
screen.title("Juego de las provincias del Ecuador")
image = "ecuador_final_map.gif"
screen.addshape(image)
screen.setup(703, 768)
turtle.shape(image)
turtle.shapesize(2,2)

#Variables globales
correct_provinces = 0
correct_provinces_list = []
#Usar el csv
province_data = pandas.read_csv("50_states.csv")

#metodo para dibujar el estado
def dibujar_provincia(provincia,xcord,ycord):
    nueva_provincia = turtle.Turtle()
    nueva_provincia.hideturtle()
    nueva_provincia.penup()
    nueva_provincia.goto(xcord,ycord)
    nueva_provincia.write(provincia)


#Metodo para detectar las coordenadas del click
def get_mouse_click_coor(x, y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)


while True:
    answer_state = (screen.textinput(title=f"{correct_provinces}/5 Provincias Correctas",
                                     prompt="Escribe el nombre de alguna provincia")).title()
    existe = (province_data['provincia'] == answer_state).any()
    if answer_state == "Exit":
        break
    if existe:
        correct_provinces_list.append(answer_state)
        resultado = province_data[province_data['provincia'] == answer_state]
        mi_variable_x = resultado['x'].iloc[0]
        mi_variable_y = resultado['y'].iloc[0]
        dibujar_provincia(answer_state, mi_variable_x, mi_variable_y)
        correct_provinces += 1


#states to learn.csv
province_data_list = province_data["provincia"].to_list()
to_learn_provinces = []
for provincia in province_data_list:
    if provincia not in correct_provinces_list:
        to_learn_provinces.append(provincia)
df_to_learn = pandas.DataFrame(to_learn_provinces)
df_to_learn.to_csv("states_to_learn.csv")
