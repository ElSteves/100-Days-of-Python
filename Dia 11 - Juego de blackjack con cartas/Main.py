# import art
# import random as rd
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# #Variables globales
# user_cards = []
# cpu_cards = []
# user_score = 0
# cpu_score = 0
# game_over = False
# def start_game():
#     global cpu_score
#     global user_score
#     # Darle 2 cartas al usuario y al cpu al inicio
#     for times in range(2):
#         user_cards.append(rd.choice(cards))
#         cpu_cards.append(rd.choice(cards))
#     # Sumar puntajes de las cartas de ambos
#     cpu_score = sum(cpu_cards)
#     user_score = sum(user_cards)
#     print_score()
#
# def append_card():
#     global user_score
#     user_cards.append(rd.choice(cards))
#     user_score = sum(user_cards)
#
# def print_score():
#     # Mostrar sus 2 cartas al usuario y mostrar una de las del cpu
#     print(f"Tus cartas: {user_cards}, puntuación actual: {user_score} ")
#     print(f"Primera carta del CPÚ: {user_cards[0]}")
#
# def comprobation():
#     global cpu_score
#     global user_score
#     global game_over
#     if user_score == 21:
#         print("Lograste un blackjack! Ganaste")
#         game_over = True
#     elif user_score > 21:
#         print("Perdiste, tu puntuacion supero los 21 puntos")
#         game_over = True
#
#
#
# want_to_play = input("Quieres jugar al blackjack? Escribe 'y' para si o 'n' para no: ").lower()
# if want_to_play == "y":
#     print(art.logo)
#     start_game()
#     while game_over == False:
#         continue_game = input("Escribe 'y' para recibir otra carta  o 'n' para dejar pasar: ")
#         if continue_game == "y":
#             append_card()
#             print_score()
#             comprobation()
#         else:
#             print(f"Tus cartas: {user_cards}, puntuación actual: {user_score} ")
#             print(f"Cartas del cpu: {cpu_cards}, puntuación del cpu: {cpu_score} ")
#             if cpu_score > user_score:
#                 print("Perdiste, el cpu tiene mas puntaje que tu.")
#             elif cpu_score == user_score:
#                 print("Empate!")
#             else:
#                 print("Ganaste!")
#             game_over = True

#Programa hecho como lo hace Angela
import art
import random as rd

def deal_card():
    """
    returns a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = rd.choice(cards)
    return card

#Funcion que retorna la suma de las cartas del mazo de los jugadores con un input de una lista
def calculate_score(cards):
    """
    Calculates the score of the given cards with a list as an input
    """
    if (len(cards) == 2) and (sum(cards) == 21):
        #Esto es un blackjack , 2 cartas que sumen 21
        return 0
    elif 11 in cards and sum(cards) >= 21: #Si hay un 11 en el mazo y las cartas son mayores a 21, el 11 se convierte en 1
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

#FUncion para calcular los scores al final del programa
def compare(u_score, computer_score):
    if u_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You lost! The cpu has a blackjack!"
    elif u_score == 0:
        return "You win! You have a blackjack!"
    elif u_score > 21:
        return "You lose! Your score is over 21"
    elif computer_score > 21:
        return "You win! The computer score is over 21!"
    elif computer_score > u_score:
        return "You lose! The computer score is greater than yours!"
    else:
        return "You win! Your score is greater than the computer score!"


def main():
    #Variables globales
    user_cards = []
    cpu_cards = []
    user_score = -1
    cpu_score = -1
    is_game_over = False

    #2 cartas del inicio para cada jugador

    for i in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)
        print(art.logo)
        print(f"Your cards: {user_cards}, your score: {user_score}")
        print(f"Computer first card: {cpu_cards[0]}")

        if user_score == 0 or cpu_score == 0 or user_score >=21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)


    print(f"Your final hand is {user_cards} and your final score is {user_score}")
    print(f"Computer's final hand is: {cpu_cards} and the final score is {cpu_score}")
    print(compare(user_score, cpu_score))

    play_again = input("Would you like to play again? (y/n): ").lower()

    if play_again == "y":
        print(".")
        main()
    else:
        print("Thank you for playing!")
        print("Exiting...")

main()

