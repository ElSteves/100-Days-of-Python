import random as rd

titulo = (""" 
 _                                              
| |                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | | 
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                    __/ |                       
                   |___/         
""")
HANGMANPICS = [''' 
  +---+ 
  |   | 
      | 
      | 
      | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
      | 
      | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
  |   | 
      | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
 /|   | 
      | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
      | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
 /    | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
 / \  | 
      | 
=========''']

#palabras a adivnar en formato de lista
palusa = ["p", "a", "l", "u", "s", "a"]
lola = ["l", "o", "l", "a"]

#Lista para contener y elegir las palabras
palabras = [lola, palusa]

#Lista con los espacios _  para imprimir mientras se va llenando
llenando = []
llenando_indice = 0
#Elegir la palabra que se usara en todo el juego

#Variable global vidas
vidas = 6
indice_hangman = 0

def elegir_palabra():
    global llenando
    palabra_elegida = rd.choice(palabras)
    for letras in palabra_elegida:
        llenando.append("_")
    return palabra_elegida

#Bajar vidas y mostrar hangman llenandose
def bajar_vidas():
    global vidas
    global indice_hangman
    vidas -= 1
    indice_hangman += 1

#Impresion de ASCII ART
def impresion():
    print(titulo)
    print(f"Tienes {vidas}/6 vidas restantes")
    print(HANGMANPICS[indice_hangman])
    print(f"Palabra a adivinar: {llenando}")


def main_juego():
    global llenando_indice
    llenando_indice = 0
    palabra_juego = elegir_palabra()
    #Impresion constante
    while vidas != 0:
        impresion()
        #Logica para llenar los espacios en blanco
        letra_input = input("Adivina una letra: ").lower()
        #Logica para perder vidas y logica para ver si no coincide con ninguna letra
        letra_encontrada = False
        for letra in palabra_juego:
            if letra == letra_input:
                letra_encontrada = True
                llenando[llenando_indice] = letra_input
            llenando_indice += 1
        if letra_encontrada == False:
            bajar_vidas()
        llenando_indice = 0
        #Logica para ganar
        if llenando == palabra_juego:
            impresion()
            print("Ganaste!")
            break
        
    if vidas == 0:
        impresion()
        print("Perdiste!")
        
#Correr el main
main_juego()

