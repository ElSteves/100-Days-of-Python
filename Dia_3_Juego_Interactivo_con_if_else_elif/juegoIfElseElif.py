print(r'''           ___
       .-'`   `'-.
   _,.'.===   ===.'.,_
  / /  .___. .___.  \ \
 / /   ( o ) ( o )   \ \                                            _
: /|    '-'___'-'    |\ ;                                          (_)
| |`\_,.-'`   `"-.,_/'| |                                          /|
| |  \             /  | |                                         /\;
| |   \           /   | | _                              ___     /\/
| |    \   __    /\   | |' `\-.-.-.-.-.-.-.-.-.-.-.-.-./`   `"-,/\/ 
| |     \ (__)  /\ `-'| |    `\ \ \ \ \ \ \ \ \ \ \ \ \`\       \/
| |      \-...-/  `-,_| |      \`\ \ \ \ \ \ \ \ \ \ \ \ \       \
| |       '---'    /  | |       | | | | | | | | | | | | | |       |
| |               |   | |       | | | | | | | | | | | | | |       |
\_/               |   \_/       | | | | | | | | | | | | | | .--.  ;Dog LOLA
                  |       .--.  | | | | | | | | | | | | | | |  | /
                   \      |  | / / / / / / / / / / / / / /  |  |/
               jgs |`-.___|  |/-'-'-'-'-'-'-'-'-'-'-'-'-'`--|  |
            ,.-----'~~;   |  |                  (_(_(______)|  |
           (_(_(_______)  |  |                        ,-----`~~~\
                    ,-----`~~~\                      (_(_(_______)
                   (_(_(_______)
''')
print("Bienvenido a Alangayork")
print("Tu mision es encontrar a Lola Palusa")
print("Estas en el parque principal, vas a Casa de lola o hacia la Iglesia?")
Path1 = input("Escribe Casa o Iglesia: \n").lower()

if Path1 == "iglesia":
    print("El padre de la iglesia penso que eras un wawa y te secuestro! Game Over")
elif Path1 == "casa":
    print("Mati esta resguardando la puerta de la casa y tienes que ahuyentarlo!")
    path2 = input("Tiras un Carne o una Piedra \n").lower()
    if path2 == "piedra":
        print("Mati golpeo la piedra con su nariz y te la devolvio. GAME OVER")
    elif path2 == "carne":
        print("Mati fue corriendo a comer la carne de cuy y dejo la puerta libre para pasar!")
        print("Entras a la casa y ves 3 puertas que dicen: \n Patty Vickie Peluchines ")
        path3 = input("Que puerta escojes? \n").lower()
        if path3 == "patty":
            print("Encontraste a Mati que te esperaba con un bate! GAME OVER")
        elif path3 == "vickie":
            print("Lola estaba acostada en la cama dormidota! LA ENCONTRASTE!")
        elif path3 == "peluchines":
            print("La puerta te llevo al universo de la familia P.Luche! TE PERDISTE!")
        else:
            print("Mija esa opcion no existe!")

    else:
        print("Mija esa opcion no existe!")
else:
    print("Mija esa opcion no existe!")

