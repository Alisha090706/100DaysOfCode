# Import the pandas library for reading CSV files and working with data
import pandas as pd

# Read the CSV file containing the NATO phonetic alphabet data into a DataFrame
data=pd.read_csv("nato.csv")

# Create a dictionary where each letter maps to its phonetic code
# Example: {'A': 'Alpha', 'B': 'Bravo', ...}
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}

# Ask the user to input a word, and convert it to uppercase
word=input("Enter a word: ").upper()

# Create a list where each letter in the word is replaced by its corresponding phonetic code
# Example: if user enters "AB", the list will be ["Alpha", "Bravo"]
def generate_phonetic_list(word):
    try:
        list=[phonetic_dict[letter] for letter in word ]
        print(list)
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed.")
        generate_phonetic_list(input("Enter a word: ").upper())
    else:
        print("Phonetic representation:", list)

generate_phonetic_list(word)