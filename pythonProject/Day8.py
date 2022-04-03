# def greet(name,location):
#     print(f"Hello {name} from {location}")
#
# greet("Priyansh Sharma","Sanawad")
# greet(name="Priyansh sharma",location="London")
# ------------------------------------------------------
# name -> Parameter At time of function declear
# while calling function what we pass is args
# Note -> We aware of order
# -----------------------------------------

# Challange1-> Paint wall
# import math
#
#
# def paint_calc(height,width,coverage):
#     no_of_cans = math.ceil((height*width)/coverage)
#     print(no_of_cans)
#
# test_h = int(input("Enter hright of wall\n"))
# test_w = int(input("Enter width of wall\n"))
# coverage = 5
# paint_calc(height=test_h,width=test_w,coverage=coverage)
# ----------------------------------------------------------------
# Challange2 = Prime number checker

# num = int(input("Enter a number\n"))
# flag = True
#
# for i in range(2,num):
#     if num%i==0:
#         flag=False
#         break
#
# if flag==True :
#     print("Its a Prime Number")
# else:
#     print("Not a prime number")

# ---------------------Prime2------------------------------
#
# num = int(input("Enter a numner\n"))
#
#
# def find_print(num):
#     count = 0
#     for i in range(2, num):
#         if num % i == 0:
#             count += 1
#             return count
#             break
#
#
# count = find_print(num=num)
# if count == 0:
#     print("Prime")
# else:
#     print("Mot prime")


# --------------------------Encrypted Password--------------------------
import Hangman

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(Hangman.logo2)
#
#
# def caeser(text_u_entered, shift_amount):
#     plain_text = ""
#     for letter in text_u_entered:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             if direction == "encode":
#                 new_position = position + shift_amount
#             elif direction == "decode":
#                 new_position = position - shift_amount
#             plain_text += alphabet[new_position]
#         else:
#             plain_text+=letter
#
#
#
#     print(f"The decoded text is {plain_text}")
#
# should_contniue = True
# while should_contniue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#
#     shift = shift % 26
#     caeser(text_u_entered=text, shift_amount=shift)
#     continue_or_not = input("Enter y for Yes n for No").lower()
#     if continue_or_not == 'n':
#         should_contniue = False
#         print("Goodbye")
#
#

print(Hangman.logo2)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
