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
def add(n1,n2):
    return n1+n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def subtract(n1,n2):
    return n1-n2
def calculator():
    print(cal)
    num1=float(input("What's the first number?: "))
    while True:
        operations={
            '+':add,
            '-':subtract,
            '*':multiply,
            '/':divide
        }
        for keys in operations:
            print(keys)
        operator=input("Choose an operation: ")
        num2=float(input("What's another number"))
        result=operations[operator](num1,num2)
        print(f"{num1}{operator}{num2}={result}")
        choice=input(f"Type 'y' to continue calculations with {result}, type 'n' to start new calculations: ").lower()
        if choice=='y':
            num1=result
        else:
            calculator()
calculator()
