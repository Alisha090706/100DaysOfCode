from resources import resources,menu
def total_amount():
    print("Please enter coins")
    cents=int(input("How many cents?: "))
    nickel=int(input("How many nickel?: "))
    dime=int(input("How many dime?: "))
    quarter=int(input("How many quarter?: "))
    total=cents*0.01+nickel*0.05+dime*0.10+quarter*0.25
    return total
def coffee_machine(choice):
    if resources['coffee']>=menu[choice]['ingredients']['coffee'] and resources['water']>=menu[choice]['ingredients']['water'] and resources['milk']>=menu[choice]['ingredients']['milk']:
        total=total_amount()
        change=round(total-menu[choice]['cost'],2)
        if change<0:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            print(f"Here is ${change} in change")
            print(f"Enjoy your {choice}☕")
            resources['water']=resources['water']-menu[choice]['ingredients']['water']
            resources['coffee']=resources['coffee']-menu[choice]['ingredients']['coffee']
            resources['money']+=menu[choice]['cost']
    else:
        print("Sorry, there is not enough resources")

while True:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {resources['money']}$")
    elif choice=='off':
        break
    else:
        coffee_machine(choice)
    
        

