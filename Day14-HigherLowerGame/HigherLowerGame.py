from data import data
import random
from os import system

highlow = ''' _  _  __  ___  _  _  ____  ____      
/ )( \(  )/ __)/ )( \(  __)(  _ \     
) __ ( )(( (_ \) __ ( ) _)  )   /     
\_)(_/(__)\___/\_)(_/(____)(__\_)     
         __     __   _  _  ____  ____ 
        (  )   /  \ / )( \(  __)(  _ \ 
        / (_/\(  O )\ /\ / ) _)  )   /
        \____/ \__/ (_/\_)(____)(__\_)'''

vs = ''' _  _  ____ 
/ )( \/ ___)
\ \/ /\___ \ 
 \__/ (____/'''

def compare(user_choice, other_choice):
    """Returns True if user_choice has more followers, otherwise False."""
    return user_choice['follower_count'] > other_choice['follower_count']

# Start game
score = 0
is_game_over = False
choice_A = random.choice(data)  # First choice before loop starts

while not is_game_over:
    print(highlow)
    
    choice_B = random.choice(data)
    while choice_A == choice_B:  # Ensure different choices
        choice_B = random.choice(data)
    
    print(f"Compare A: {choice_A['name']}, {choice_A['description']}, from {choice_A['country']}")
    print(vs)
    print(f"Against B: {choice_B['name']}, {choice_B['description']}, from {choice_B['country']}")
    
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice == 'A':
        result = compare(choice_A, choice_B)
    else:
        result = compare(choice_B, choice_A)

    system('cls')  # Clear screen

    if result:
        score += 1
        print(f"You got it right! Your score: {score}")
        choice_A = choice_B  # Move the correct choice forward
    else:
        is_game_over = True
        print(f"Sorry, you got it wrong. Final score: {score}")
