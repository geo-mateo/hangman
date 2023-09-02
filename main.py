import random

print("Welcome to Hangman!")

words = ["hacker", "bounty", "random"]
#Create an empty list
#For each letter in the secret_word add a "_" that will be
#         printed to the console
#Example if the word is Hacker "_","_","_","_","_","_"

secret_word = random.choice(words)
display_word = []
for lett in secret_word:
    display_word += "_"
print(display_word)

guess = input("Geuss a letter").lower()
#Loop through each if the letters in the chosen word
#if the letter is in the word replace the "_" with the letter
#it should look like this "_","a","c","_","_","r"


for position in range(len(secret_word)):
    letter = secret_word[position]
    if letter == guess:
        display_word[position] = letter
print(display_word)