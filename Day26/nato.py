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
list=[]
for letter in word:
    try:
        list.append(phonetic_dict[letter])
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed.")
        break
print(list)

