import random
print('''
  ___  _  _  ____  ____  ____    ____  _  _  ____    __ _  _  _  _  _  ____  ____  ____ 
 / __)/ )( \(  __)/ ___)/ ___)  (_  _)/ )( \(  __)  (  ( \/ )( \( \/ )(  _ \(  __)(  _ \ 
( (_ \) \/ ( ) _) \___ \\___ \    )(  ) __ ( ) _)   /    /) \/ (/ \/ \ ) _ ( ) _)  )   /
 \___/\____/(____)(____/(____/   (__) \_)(_/(____)  \_)__)\____/\_)(_/(____/(____)(__\_)
''')
def guess_number(lives,number):
    while lives!=0:
        print(f"You have {lives} attempts remaining to guess the number")
        user_choice=int(input("Make a choice: "))
        if user_choice<number:
            print("Too Low")
        elif user_choice==number:
            print("You guessed the number!")
            return
        else:
            print("Too High")
        lives-=1
        if lives==0:
            print("You ran out of lives. You lose!")
            print(f"The number was {number}")
            return

print("Welcome TO number Guessing Game")
number=random.randint(1,100)
print("I am thinking of a number between 1 and 100")
difficulty=input("Choose difficulty. Type 'easy' or 'hard': ").lower()
if difficulty=='easy':
    guess_number(10,number)
else:
    guess_number(5,number) 

