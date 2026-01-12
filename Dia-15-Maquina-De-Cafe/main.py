#Datos
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": float(0),
}

#from resources_data import resources, MENU

option = ""
successful_transaction = False
can_make = False
inserted_money = 0.0

def resources_sufficient(u_option):
    global can_make
    for ingredient in MENU[u_option]["ingredients"]:
        if MENU[u_option]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there isn´t enough {ingredient}")
            can_make = False
            break
        else:
            can_make = True

def make_coffe(u_option):
    for ingredient in MENU[u_option]["ingredients"]:
        resources[ingredient] -= MENU[u_option]["ingredients"][ingredient]
    #Agregar ganancia al monto de la maquina
    resources["money"] += MENU[u_option]["cost"]
    print(f"Making {u_option}\n Here it is! Enjoy your {u_option}")

def insert_coins():
    quarters = int(input("How many quarters 0.25$ do you want to enter: "))
    dimes = int(input("How many dimes 0.10$ do you want to enter: "))
    nickles = int(input("How many nickles 0.05$ do you want to enter: "))
    pennies = int(input("How many pennies 0.01$ do you want to enter: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

while option != "off":
    option = input("What would you like? espresso/latte/cappuccino: ").lower()
    #TODO: 3. Print report
    if option == "report":
        for item in resources:
            print(f"{item.title()}: {resources[item]}")
    elif option in MENU:
        #Comprobar si se puede hacer el cafe
        resources_sufficient(option)
        #Hacer el cafe
        if can_make:
            inserted_money = insert_coins()
            if inserted_money == MENU[option]["cost"]:
                make_coffe(option)
            elif inserted_money > MENU[option]["cost"]:
                change = inserted_money - MENU[option]["cost"]
                print(f"Here is your change: {round(change, 2)}$")
                make_coffe(option)
            else:
                print(f"Sorry that's not enough money. {inserted_money}$ refunded.")
#Apagar la maquina de cafe
print("Turning off...")




