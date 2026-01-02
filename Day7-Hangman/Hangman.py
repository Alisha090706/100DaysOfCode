hangman_stages = [
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    (Game Over)
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """
]

words = [
    "python", "developer", "keyboard", "monitor", "programming",
    "laptop", "interface", "database", "algorithm", "function",
    "variable", "internet", "software", "hardware", "framework",
    "debugging", "compiler", "cybersecurity", "network", "server",
    "artificial", "intelligence", "machine", "learning", "automation",
    "repository", "frontend", "backend", "fullstack", "encryption",
    "authentication", "authorization", "javascript", "typescript"
]

import random
placeholder=""
word=random.choice(words)
for i in range(len(word)):
    placeholder+="_"
print(placeholder)
lives=6
correct_letters=[]
game_over=False
while not game_over:
    display=""
    choice=input("Enter a letter: ").lower()
    for letter in word:
        if choice==letter:
            display+=letter
            correct_letters.append(choice)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
    if choice not in word:
        lives-=1
        if lives==0:
            print("YOU LOSE!")
            game_over=True
    if "_" not in display:
        print('YOU WIN!')
        game_over=True
    print(hangman_stages[lives])
print(f"The word was: {word}")