import random as rn
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

computer_choice=rn.randint(0,2)
list=[rock,paper,scissors]
user_choice=int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print("Your choice:")
print(list[user_choice])
print("Computer's choice:")
print(list[computer_choice])
if user_choice==computer_choice:
    print("It's a draw!")
elif computer_choice==0 and user_choice==2:
    print("You Lose!")
elif user_choice==0 and computer_choice==2:
    print("You Win!")
elif user_choice<computer_choice:
    print('You lose!')
elif user_choice>computer_choice:
    print("You Win!")
else:
    print("Invalid input. You lose!")