def add(n1, n2):
    return n1 + n2

#TODO: Write the other 3 functions -subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#TODO: Add these 4 functions into a dictionary as the values, Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#TODO: Use the dictionary operations to perform the calculations. Multiply 4*8 Using the dictionary


# print(operations["*"](4,8))
continue_with_result = "n"
#completar
while True:
    if continue_with_result == "n":
        print("\n"*20)
        first_number = float(input("Type the first number: "))
        print("""
        +
        -
        *
        /""")
        math_operator = str(input("Type an operator: "))
        second_number = float(input("Type the second number: "))
        result = operations[math_operator](first_number,second_number)
        print(f"{first_number} {math_operator} {second_number} = {result}")
        continue_with_result = input(f"Do you want to continue working with the previus result of {result}? types 'y' or type 'n' to start a new calculation")
    elif continue_with_result == "y":
        print("""+
                -
                *
                /""")
        math_operator = str(input("Type an operator: "))
        second_number = float(input("Type the second number: "))
        result = operations[math_operator](result, second_number)
        print(f"{math_operator} {second_number} = {result}")
        continue_with_result = input(f"Do you want to continue working with the previus result of {result}? types 'y' or type 'n' to start a new calculation")
