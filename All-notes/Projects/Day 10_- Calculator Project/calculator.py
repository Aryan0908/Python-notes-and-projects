# Calculator
import calculator_art

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multipy(n1, n2):
    return n1 * n2

def calculator():
    print(calculator_art.logo)
    n1 = float(input("What is the first number? "))

    mathematical_operators = {
        "+": add, 
        "-": substract,
        "/": divide,
        "*": multipy
    } 

    for key in mathematical_operators:
        print(key)

    symbol = input("From the above mathematical operators pick any one? ")

    n2 = float(input("What is the second number? "))


    answer = mathematical_operators[symbol](n1, n2)
    final_output = print(f"{n1} {symbol} {n2} = {answer}")





    user_choice = True
    while user_choice == True:
        continue_operation = input(f"Type 'Y' to add more operations to{answer} or 'N' to start a new calculator.").lower()
        if continue_operation == "y":
            for key in mathematical_operators:
                print(key)
            new_symbol = input("From the above mathematical operators pick any one? ")
        
            n3 = float(input("What is the new number? "))
        
            new_answer = mathematical_operators[new_symbol](answer, n3)
        
            final_output = print(f"{answer} {new_symbol} {n3} = {new_answer}")
        
            answer = new_answer
        
        elif continue_operation == "n":
            user_choice = False
            calculator()
        
calculator()
        