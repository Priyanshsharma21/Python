# Rules->
# 1. We have  cards its sum must be 21 then we will win the game
# 2. 1-10 count as face value
# queen king and jack count as 10
# A ace count as 11 or 1 you decide
# At first dealer and us have a single card which is revealed
# Dealer pick a second card unrevealed
# we pick a card and if that card sum is 21 than we win if more than 21 we loose
# If both score is same than draw
# If dealer have sum of card under 17 (1-16) then he can pick another card
# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ------------------------Start-------------------------
# import Hangman
# import random
#
# yon = input("Do you want to play blackjack game? Type y or n \n").lower()
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# if yon == 'y':
#     print(Hangman.logo5)
#     card1 = random.choice(cards)
#     card2 = random.choice(cards)
#     card3 = random.choice(cards)
#
#     compCard = random.choice(cards)
#     compCard2 = random.choice(cards)
#     compCard3 = random.choice(cards)
#
#     print(f"Your current cards are [{card1},{card2}], Current score is: {card1 + card2}")
#     print(f"Computer first card is : {compCard}")
#
#     addCard = input("Type 'y' to add another card type 'n' to pass\n").lower()
#     if addCard == 'y':
#
#
#
#         yourScore2 = card1 + card2 + card3
#         compScore2 = compCard + compCard2
#         print(f"Your current cards are [{card1},{card2} {card3}], Current score is: {card1 + card2 + card3}")
#         print(f"Computer second card is : {compCard2}")
#         print(f"Computer final hand is [{compCard},{compCard2}], Second score is {compCard + compCard2}")
#
#
#
#         if compScore2 > yourScore2:
#             print(f"Computer score is {compScore2} and your score is {yourScore2}")
#             print("Computer wins!!")
#         elif yourScore2 > compScore2:
#             if yourScore2<21:
#                  print(f"Computer score is {compScore2} and your score is {yourScore2}")
#                  print("You won won!!")
#             else:
#                 print(f"Your score is {yourScore2} you pass the limit hance loose")
#         else:
#             print("Match Draw!!!")
#
#
#
#
#
#
#
#     else:
#         yourScore1 = card1 + card2
#         compScore1 = compCard + compCard2
#         print(f"Your final hand is [{card1},{card2}], Final score is: {card1 + card2}")
#         print(f"Computer final score is [{compCard},{compCard2}], Final score is: {compCard + compCard2}")
#         if compScore1 > yourScore1:
#             print(f"Computer score is {compScore1} and your score is {yourScore1}")
#             print("Computer wins!!")
#         elif yourScore1 > compScore1:
#             print(f"Computer score is {compScore1} and your score is {yourScore1}")
#             print("You won won!!")
#         else:
#             print("Match Draw!!!")
#

# -------------------------------Maidam ka solution-------------------------------------
import random
import Hangman


def deal_Card():
    """Return a card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_card(cards):
    if sum(cards) == 21 and len(cards) == 21:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userScore,compScore):
    if userScore==compScore:
        return "Draw"
    elif compScore==0:
        return "lose, Computer has a BlackJack"
    elif userScore==0:
        return "Won, You had a Blackjack"
    elif userScore>21:
        return "your, Limit pass, You loose"
    elif compScore>21:
        return "computer, Limit pass, You won"
    elif userScore>compScore:
        return "You win!!😁"
    else:
        return "Computer won!!👽"


userCard = []
compCard = []
isgameOver = False

for _ in range(2):
    newCard = deal_Card()
    userCard.append(newCard)
    computerCard = deal_Card()
    compCard.append(computerCard)

while not isgameOver:

    userScore = calculate_card(userCard)
    compScore = calculate_card(compCard)

    print(f"Your card is {userCard} , current Score is {userScore}")
    print(f"Computer's first card: {compCard[0]}")

    if userScore == 0 or compScore == 0 or userScore > 21:
        isgameOver = True
    else:
        user_should_deal = input("Type 'y' to add another card, type 'n' to pass:")

        if user_should_deal == 'y':
            userCard.append(deal_Card())
        else:
            isgameOver = True


while compScore!=0 and compScore<17:
    compCard.append(deal_Card())
    compScore = calculate_card(compCard)

compare(userScore,compScore)

# --------------------------------------------------------------------------------------/
import random
from replit import clear
from Hangman import logo4

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo4)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()