import random
import Hangman
import replit



def choossePerson():
    """This function choose the random person from data"""
    randomPerson = random.choice(Hangman.data)
    return randomPerson


def personDetail(randomPerson):
    """This function give us the detail of person expect there followers"""
    return f"{randomPerson['name']}, {randomPerson['description']}, {randomPerson['country']}"


def comparePerson(guess,a_follower,b_follower):
    if a_follower>b_follower:
        return guess=='a'
    else:
        return guess=='b'

def game():
    print(Hangman.logo7)
    currentScore = 0
    continueGame = True
    person2 = choossePerson()

    while continueGame:
        person1 = person2
        person2 = choossePerson()

        while person1==person2:
            person2 = choossePerson()

        print(f"Compare A: {personDetail(person1)}.")
        print(Hangman.vs)
        print(f"Against B: {personDetail(person2)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        isCorrect = comparePerson(guess,person1['follower_count'],person2['follower_count'])

        replit.clear()

        if isCorrect:
            currentScore+=1
            print(f"You're right! Current score: {currentScore}.")
        else:
            continueGame = False
            print(f"Sorry, that's wrong. Final score: {currentScore}")



game()



