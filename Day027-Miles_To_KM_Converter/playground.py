### This file is for learning and experimenting with Python code snippets. ###

### Topic : Args And Kwargs ###

### Args and Kwargs are used in function definitions to allow for variable numbers of arguments.

### *args allows a function to accept any number of positional arguments.
def add_numbers(*args):
    sum=0
    for num in args:
        sum+=num
    return sum

print(add_numbers(1,2,3))  # Output: 6
print(add_numbers(5,10,15,20))  # Output: 50


### **kwargs allows a function to accept any number of keyword arguments.
def calculate(n,**kwargs):
    n+=kwargs.get("add",0)
    n*=kwargs.get("multiply",1)
    return n
print(calculate(2,add=3))  # Output: 5


class Car:
    def __init__(self,**kwargs):
        self.make=kwargs.get("make")
        self.model=kwargs.get("model")

my_car=Car(make="Nissan", model="Altima")
print(my_car.make)

car2=Car(make="Honda")
print(car2.model)