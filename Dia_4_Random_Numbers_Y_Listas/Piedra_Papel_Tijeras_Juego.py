import random as rd
#ASCCI ART
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]
print("Juego de piedra, papel o tijeras.")
decision = int(input("Elige una opcion: 1 para piedra, 2 para papel y 3 para tijeras\n"))
if decision>=1 and decision<=3:
    print(game_images[decision-1])
print("Decision de BOT")
decision_bot = rd.randint(1,3)
print(game_images[decision_bot-1])
#Logica de WIN OR LOSE
if decision_bot == decision:
    print("Empate!")
elif (decision_bot == 1 and decision == 3) or (decision_bot == 2 and decision == 3) or (decision_bot == 3 and decision == 1):
    print("Ganaste!")
elif (decision_bot == 3 and decision == 1) or (decision_bot == 3 and decision == 2) or (decision_bot == 1 and decision == 3):
    print("Perdiste!")
else:
    print("Error, escogiste una opcion que no existe!")


