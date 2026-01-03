from os import system
print(''' ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\ 
                         `'-------'`
                       .-------------.
                      /_______________\ ''')
silent_auction={}
print("Welcome to the Secret Auction Program")
while True:
    name=input("What is your name?: ")
    bid=int(input("What's your bid today?: $"))
    silent_auction[name]=bid
    bidders=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if bidders=='no':
        system("cls")
        break
    else:
        system("cls")
max=0
for key in silent_auction:
    if silent_auction[key]>max:
        max=silent_auction[key]
        winner=key
print(f"The winner is {winner} with bid ${max}")
