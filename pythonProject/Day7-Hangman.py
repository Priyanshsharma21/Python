# Flowchart
# 1. Take a random number from user
# 2. Create blank space equal to number of words in the random choosen work
# 3. Ask user to guess the letter
# 4. If -> is the guess word in the letter then replace the - position with word
# 5. Else -> Loose a life
# 6. check->If all the blanks are filled then -> if no then repeat(3-5)
#                                               else won the game

# 6. check-> If all the life looses -> if yes -> game over, if no then repeat(3-5)

# lets gooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# ----------------------------------Version1.0--------------------
# # Task1 -> Take a random number from user
# import random
#
# words = ["camel", "orange", "barbell"]
# hint = ["king of desert", "Name = Color fruit", "Gym"]
# # Task2-> choose random word
#
# randomNumber = random.randint(0, len(words) - 1)
# chosen_Word = words[randomNumber]
# chosen_hint = hint[randomNumber]
# print(f"Hint : {chosen_hint}")
#
# # Task3-> Ask uer to guess the letter
# print("Note : Enter word at a time\n")
# guess = input("Guess the letter:\n").lower()
#
# # Task4-> Check is the letter chosen is one in the list
#
# word_split = list(chosen_Word)
#
# for i in word_split:
#     if i==guess:
#         print("Right")
#     else:
#         print("Wrong")
#

# --------------------Version2.0-----------------------------
#
# import random
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# words = ["camel", "orange", "barbell"]
# hint = ["king of desert", "Name = Color fruit", "Gym"]
#
# randomNumber = random.randint(0, len(words) - 1)
# chosen_Word = words[randomNumber]
# chosen_hint = hint[randomNumber]
# print(f"Chossen Word is {chosen_Word}")
# print(f"Hint : {chosen_hint}")
#
#
# display = []
# for _ in range(len(chosen_Word)):
#     display += "_"
#
# print("Note : Enter word at a time")
#
# word_split = list(chosen_Word)
#
# # Task2 -> Replace the empty space in display with the gusee letter
# end_of_game = False
# no_Of_Lives = 6
#
# while not end_of_game:
#     guess = input("Guess the letter:\n").lower()
#     for position in range(len(word_split)):
#         letter = word_split[position]
#         if letter == guess:
#             display[position] = letter
#
#     if guess not in word_split:
#         no_Of_Lives -= 1
#         if no_Of_Lives == 0:
#             end_of_game = True
#             print("You Lose")
#     print(f"{''.join(display)}")
#
#     if "_" not in display:
#         end_of_game = True
#         print("Won!!!!")
#
# ----------------------Version3.0------------------------

import random
import Hangman
from replit import clear



end_of_game = False
words = Hangman.words
hint = Hangman.hint
stages = Hangman.stages
logo = Hangman.logo
print(logo)
randomNumber = random.randint(0, len(words) - 1)
chosen_Word = words[randomNumber]
chosen_hint = hint[randomNumber]
word_length = len(chosen_Word)

lives = 6


display = []

for _ in range(word_length):
    display += "_"

print(f"Hint:{chosen_hint}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess==display:
        print(f"You already gussed the {guess} letter")

    for position in range(word_length):
        letter = chosen_Word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_Word:
        print(f"This letter is not in the Word, Loose life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Khatam Khallas Bye Bye.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])