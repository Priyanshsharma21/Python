# Bug->
############DEBUGGING#####################

# # Describe Problem
"""Range function runs from 'lower bound - upper bound-1' heance message not printed
So make 20-21"""
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()


# # Reproduce the Bug -> Error that we get ocassionaly
"""You run your code once twice but at sme point of time you get a error"""
"""Radiant or any random function take lower and upper both bound"""
"""Hence make1->0 and 6 -> 5, so no index out of bound"""
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])


# # Play Computer
"""Read code like you are computer
make < or > to <= and >= because in case of < or > it will not print any statemant
"""
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")


# # Fix the Errors
"""Indentation errror -> fix by a tab
next error in this is age is a integer and we give string default
next error is use fString"""
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")


# #Print is Your Friend
"""First of all we are using the == check sign so value check to it not assign
Use Print statement to actually know the problem where exist"""
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# # print(pages)
# # print(word_per_page)
# print(total_words)


# #Use a Debugger
"""Always remember and concious about indentation"""
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])

# ------------------Tips------------------------
# 1. Stop staring to the code & take a break when not knows about problem
# 2. Run Code ofter -> at every single step you execute
# 3. StackOverflow

# ------------------------More Debugg----------------
# number = int(input("Which number do you want to check?"))
#
# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")


# year = int(input("Which year do you want to check?"))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])
