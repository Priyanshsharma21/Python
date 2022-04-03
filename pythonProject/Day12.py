# Scope
# Local scope exist inside the function, so variable declear inside the function are local scoped
# Global scope exist outside the function, Variable declear outside the function is global scoped
# Whatever we name like (variable,function) have scope and this apply to all
# If you create an variable inside the if or for or while then that dont count as a local scope
# It can be used outside

# If you create a variable outside def it is global and if you create same name function  the
# inside the fuinction it is completly different variale
# ex ->

# itsMe = 0
# PI = 3.14 # Constants are decleared with uppercase
# def increase():
#     # global itsMe # must be avoid in case of variable but in case of constant must be used
#     # itsMe+=1
#     print(itsMe)
#     return itsMe + 1

# --------------------Guess The Number------------------------
import random
import Hangman
print(Hangman.logo6)
jackNum = random.randint(1, 100)
print("Welcome to the number Guessing Game: ")
print("I'am thinking of a number between 1 & 100")
defficulty = input("Choose the difficulty level. 'Easy' or 'Hard'").lower()

def rules():
    print("""You Can Enter Number Between 1 & 100 Only Thank You.😁""")



if defficulty=='easy':
    attempt = 10
    while attempt !=0:
        print(f"--------------------------------->Attempt number {attempt}")
        playerGuess = int(input("Guess the Jacks Number: "))

        if playerGuess==jackNum:
            print("You got the Number😁👍")
            break
        elif playerGuess>jackNum:
            print("Jack Says Little Low: ")
        elif playerGuess<jackNum:
            print("Jack Says Little High")
        else:
            print("Plese enter correct number: ")
            rules = input("Press 'r' to know the game rules: ").lower()
            if rules=='r':
                rules()
        attempt-=1
    print(f"Game Over🎮")
    print(f"Jack's Number was {jackNum}, Try Again")

else:
    attempt = 5
    while attempt != 0:
        print(f"--------------------------------->Attempt number {attempt}")
        playerGuess = int(input("Guess the Jacks Number: "))

        if playerGuess == jackNum:
            print("You got the Number😁👍")
            break
        elif playerGuess > jackNum:
            print("Jack Says Little Low: ")
        elif playerGuess < jackNum:
            print("Jack Says Little High")
        else:
            print("Plese enter correct number: ")
            rules = input("Press 'r' to know the game rules: ").lower()
            if rules == 'r':
                rules()
        attempt -= 1
    print(f"Game Over🎮")
    print(f"Jack's Number was {jackNum}, Try Again")


# -----------------Angela Baind Solution------------------------
# from random import randint
# from art import logo
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")
#
# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS
#
# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}")
#
#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")
#
#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))
#
#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")
#
#
# game()



