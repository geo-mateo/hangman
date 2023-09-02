import random

print("Welcome to Hangman!")

words = ["hacker", "bounty", "random"]


secret_word = random.choice(words)
print(secret_word)
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)


#1 use a while loop word has been keeps going
# until the word has been guessed

game_over = False

while not game_over:
    guess = input("Geuss a letter").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    print(display_word)

    if "_" not in display_word:
        print("You Won")
        game_over = True