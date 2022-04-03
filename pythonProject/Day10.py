# Function with output
# -------------------Calculaor--------------------
# def add(num1, num2):
#     return num1 + num2
#
#
# def subtract(num1, num2):
#     return num2 - num1
#
#
# def mult(num1, num2):
#     return num1 * num2
#
#
# def divide(num1, num2):
#     return num2 / num1
#
# num1 = int(input("Enter a number1: "))
# num2 = int(input("Enter a number2: "))
# print(""" +
#           -
#           *
#           /""")
# symbole = input("What calculation you wanna do: ")
#
#
# if symbole== "+":
#     result = add(num1=num1,num2=num2)
#     print(f"Sum of numbers is {result}")
# elif symbole=="-":
#     result = subtract(num1=num1, num2=num2)
#     print(f"Subtraction of numbers is {result}")
# elif symbole=="*":
#     result = mult(num1=num1, num2=num2)
#     print(f"Multiplication of numbers is {result}")
# elif symbole=="/":
#     result = divide(num1=num1, num2=num2)
#     print(f"Division of numbers is {result}")

# --------------------------------------------------------------------
#
# def print_upper(f_name,l_name):
#     title_f_name = f_name.title()
#     title_l_name = l_name.title()
#     return {f"First name is {title_f_name} and last name is {title_l_name}"}
#
# op = print_upper("PriYansH","ShArmA")
# print(op)

# Note -> After return no line will be executed

# -----------------------Challange 2 - Days in a month---------------

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(years,months):
#     """This function will return number of days in the month of a particular year
#     pass year and month in it and it will show you the days in that month"""
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(years):
#         if months==2:
#             return 29
#     else :
#         return month_days[month-1]
#
#
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(f"There are {days} in that month")

# -----------------Boss Challange-------Calculator-------------------------
# import Hangman
#
# print(Hangman.logo4)
#
#
# def add(num1, num2):
#     return num1 + num2
#
#
# def subtract(num1, num2):
#     return num2 - num1
#
#
# def mult(num1, num2):
#     return num1 * num2
#
#
# def divide(num1, num2):
#     return num2 / num1
#
#
# operation = {"+": add, "-": subtract, "*": mult, "/": divide}
# num1 = int(input("Enter a number1: "))
#
# for symbole in operation:
#     print(symbole)
# operator_symbole = input("What calculation you wanna do: ")
# num2 = int(input("Enter a number2: "))
# Calculation_function = operation[symbole]
# answer1 = Calculation_function(num1,num2)
# print(f"Calculating {num1} {operator_symbole} {num2} = {answer1}")
#
# flag = True
#
# while flag:
#     deside = input(f"If you wanna perform More operation on {answer1} 'yes' or 'no' you deside").lower()
#     if deside=="yes":
#         operator_symbole = input("What calculation you wanna do: ")
#         num3 = int(input("Enter a number2: "))
#         answer2 = Calculation_function(Calculation_function(num1, num2), num3)
#         print(f"Calculating {num1} {operator_symbole} {num3} = {answer2}")
#     else:
#         flag=False
#
#

from replit import clear
import Hangman




def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(Hangman.logo4)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()




