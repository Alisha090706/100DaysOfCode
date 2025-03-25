import random
blackjack='''  ____  _            _    _            _    
 |  _ \| |          | |  (_)          | |   
 | |_) | | __ _  ___| | ___  __ _  ___| | __
 |  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   <| | (_| | (__|   < 
 |____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                        _/ |                
                       |__/                 
'''        

play=input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
def calculate_score(lst):
    if sum(lst)==21 and len(lst)==2:
        return 0
    if sum(lst)>21 and 11 in lst:
        lst.remove(11)
        lst.append(1)
    return sum(lst)
def deal_card():
    card_deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(card_deck)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return 'DRAW🙃'
    elif computer_score==0:
        return "YOU LOSE😥. COMPUTER HAS BLACKJACK"
    elif user_score==0:
        return "YOU WIN🏆 WITH A BLACKJACK"
    elif user_score>21:
        return "YOU LOSE😭. YOU WENT OVER"
    elif computer_score>21:
        return "COMPUTER WENT OVER. YOU WIN🏆"
    elif user_score>computer_score:
        return "YOU WIN🏆"
    else:
        return "YOU LOSE😭"
while play=='y':
    print(blackjack)
    user_card=[]
    computer_card=[]
    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    is_game_over=False
    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print("Your card: ",user_card)
        print("Your score: ",user_score)
        print("Computer's first card: ",computer_card[0])
        if calculate_score(user_card)==0 or calculate_score(computer_card)==0 or calculate_score(user_card)>21:
            is_game_over=True
        else:
            user_next_card=input("Do you wish to take another card? Type 'y' or 'n': ").lower()
            if user_next_card=='n':
                is_game_over=True
            else:
                user_card.append(deal_card())
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    print(f"Your final card: {user_card} and score :{user_score}")
    print(f"Compter final card: {computer_card} and score: {computer_score}")
    print(compare(user_score,computer_score))
    play=input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    print("\n"*20)