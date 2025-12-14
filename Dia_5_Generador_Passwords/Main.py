import random as rd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level
#password = "" #contraseña vacia
#total_characters = nr_numbers + nr_symbols + nr_letters
#for letter in range(0,total_characters):
    #if nr_letters != 0:
     #   random_num = rd.randint(0,len(letters)-1)
      #  password += letters[random_num]
       # nr_letters -= 1
    #elif nr_symbols != 0:
     #   random_num = rd.randint(0,len(symbols)-1)
      #  password += symbols[random_num]
       # nr_symbols -= 1
    #elif nr_numbers != 0:
     #   random_num = rd.randint(0,len(numbers)-1)
      #  password += numbers[random_num]
       # nr_numbers -= 1
#print(f"Your password could be : {password}")

#Hard version Using lists
password = [] #lista para la contraseña vacia
#Logica simplificada a 3 fors con el rango dado y usando menos lineas
for _ in range(nr_letters):
    password.append(rd.choice(letters))

for _ in range(nr_symbols):
    password.append(rd.choice(symbols))

for _ in range(nr_numbers):
    password.append(rd.choice(numbers))
#Con lo de arriba guardamos la contraseña en una lista de caracteres que podemos shuflear
#No es posible shuflear un string como tal
rd.shuffle(password) #Shuflea con la biblioteca random una lista
password = "".join(password)    #Junta los elementos de la lista en un string
print(f"Your password could be : {password}")





