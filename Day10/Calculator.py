cal=''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|'''
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
def calculator():
    print(cal)
    operations={
        '+':add,
        '-':subtract,
        '*':multiply,
        '/':divide
    }
    first_number=float(input("What is your first number?: "))
    while True:    
        for keys in operations:
            print(keys)
        operator=input("Pick an operation: ")
        second_number=float(input("What's the next number?: "))
        result=operations[operator](first_number,second_number)
        print(f"{first_number}{operator}{second_number}={result}")
        choice=input(f"Type 'y' to continue calculating with {result} , or type 'n' to start a new calculation: ").lower()
        if choice=='n':
            calculator()
        else:
            first_number=result
            
calculator()