import random

#create a greeting

print("Welcome to Hangman!")

#create your word list

words = ["hacker", "bounty", "random"]

#randomly choose a word from the list you have created

secret_word = random.choice(words)

#ask the user to gueass a letter

guess = input("Geuss a letter").lower()
print(guess)

#check if the letter id in the word

for letter in secret_word:
    if letter ==guess:
        print("Right")
    else:
        print("Wrong")