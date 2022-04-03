# import random

# 1.# Module is whatever code we wrote which have its functionality we can imort that module and use its functionality anywhere
# Howto use it -> Just import the part of your code ex -> Import day1 // and use it

# 1. Randomization
# randomNum = random.randint(100, 1000)
# print(randomNum)
# # Generate Random number between numbers include start and end points (int)
# randomNum2 = random.random() * 100
# print(randomNum2)
# generate float


# ex1 -> head mai jita tail tu hara

# desision = random.randint(1, 2)
#
# if desision == 1:
#     print("Head")
# else:
#     print("Tail")

# List -> used to Store related data(ds) in an order. like a array

# state = ['MP','Maharashtra','gujrat']
# print(state[2])
# state[2] = 'chattisghard'
# print(state[2])
# state.append("piyuLand")
# state.extend(["shreyuland","aarajuland"])
# print(state)

# ex2->
# people = input("Enter names of people")
# listOfPeople = people.split(" ")
# biller = random.randint(1, listOfPeople-1)
# print(f"Today {listOfPeople[biller]} will pay the bill")

# or

# names = ['priyansh','shreyansh','poonam','sushil']
# whowillpay = random.choice(names)
# print(whowillpay)

# 3. Nested list
# chest = ["bench press","crossover","Chest Press","Dumbell Flys","Smith Machine Press"]
# back = ["Latpulldown","Pullups","Single arm dumbell rows","Chest supported rows"]
# leg = ["barbell Squads","leg press","leg extentions","hamstring curls","calf raises"]
#
# list1 = [chest,back,leg]
# print(list1[2][2])

# Note -> In list index start from 0 to list-1
# and from behind -1

import random
# challange -> Rock paper scissor
cpu = ["R","P","S"]
itsHerChoice = random.randint(0,2)
herchoice  = cpu[itsHerChoice]
mychoice = input("Enter R-Rock, P-paper, S-scissor")
R = 	("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

P = 	("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

S =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("Your choice is: "+mychoice)
print("CPU choice is:"+herchoice)

if mychoice=='R':
    print(R)
    if herchoice=='R':
        print(R)
        print("Tied")
    elif herchoice=='P':
        print(P)
        print("You Won")
    else:
        print(S)
        print("You Lose")


elif mychoice=='P':
    print(P)
    if herchoice=='R':
        print(R)
        print("you lose")
    elif herchoice=='P':
        print(P)
        print("Tied")
    else:
        print(S)
        print("You Won")

else:
    print(S)
    if herchoice=='R':
        print(R)
        print("You loose")
    elif herchoice=='P':
        print(P)
        print("You Won")
    else:
        print(S)
        print("Tied")