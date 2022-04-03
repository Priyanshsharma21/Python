# from art import *

# Conditional
# ex1-> ticket 1.0
# height = int(input("Enter your height: "))
# if (height<120):
#     print("You are not eligible for this ride")
# else:
#     print("Welcome to this ride")

# ex2-> odd even

# n = int(input("Enter a number: "));
#
# if(n%2==0):
#     print(str(n) + " is even.")
# else:
#     print(str(n) + " is odd.")


# ex3 -> ticket 2.0

# height = int(input("Enter your height: "))
# age = int(input("Enter your age: "))
#
# if height>=120:
#     if age>18:
#         print("welcome, you have to pay 18$")
#     elif age<12:
#         print("Welcome pay 12$")
#     elif age>12 and age<18:
#         print("Aayea swagad hai aap ka paan parag se")
#
# else:
#     print("i'm Sorry bro")

# ex-> BMI 2.0
# height = float(input("Enter your height(cm): "))
# weight = float(input("Enter your weight(kg)"))
# cmh = height/100;
#
# bmi = weight/cmh**2
# print(bmi)
#
# if bmi<18.5:
#     print("Underweight")
# elif bmi>18.5 or bmi<=24:
#     print("Normal Weight")
# elif bmi>24 or bmi<27:
#     print("Overweight")
# elif bmi>27:
#     print("Obease")

# ex5-> leap year

# year = int(input("Enter a year: "))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Leap year")
# else:
#     print("not a leap year")
#
# # or
#
# for year in range(5000):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print("Leap year")
#     else:
#         print("not a leap year")
#


# ex6-> Ticket 2.0
#
# height = int(input("Enter your height: "))
# bill = 0
#
# if height >= 120:
#     print("You can ride Columbus")
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         print("Welcome, you have to pay 18$-(Adult ticket)")
#         bill = 18
#     elif age < 12:
#         print("Welcome pay 12$-(child ticket)")
#         bill = 12
#     elif 12 < age < 18:
#         print("Welcome Pay 15$-(Teen ticket)")
#         bill = 15
#     yorn = input("Do you want photo: y for yes, n for no")
#     if yorn=='y':
#         bill+=3
#
#     print("Your total is"+str(bill))
# else:
#     print("i'm Sorry bro")


# ex7-> Pizza order
# print("Welcome to Pizza Bean 🍕😋")
# size = input("What size pizza you want, S for Small, M for Medium, L for large")
# add_peporani = input("Do you want Peporani, Y or N")
# add_cheese = input("Do you like to have extra cheese, Y or N")
# bill = 0
#
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# else:
#     bill += 25
#
# if add_peporani=='Y':
#     if size=='S':
#         bill+=2
#     else :
#         bill+=3
#
# if add_cheese=='Y':
#     bill+=1
#
# print(f"Your final bill is {bill}")


# ex-> Ticket bill 4.0
#
# height = int(input("Enter your height: "))
# bill = 0
#
# if height >= 120:
#     print("You can ride Columbus")
#     age = int(input("Enter your age: "))
#     if age >= 18 and age<45:
#         print("Welcome, you have to pay 18$-(Adult ticket)")
#         bill = 18
#     elif age < 12:
#         print("Welcome pay 12$-(child ticket)")
#         bill = 12
#     elif 12 < age < 18:
#         print("Welcome Pay 15$-(Teen ticket)")
#         bill = 15
#     elif age>=45 and age<=55:
#         print("This ride is free for you but not photo so:")
#         bill=0;
#     yorn = input("Do you want photo: y for yes, n for no")
#     if yorn=='y':
#         bill+=3
#
#     print("Your total is"+str(bill))
# else:
#     print("i'm Sorry bro")


# ex-> Oh My God Turu Lovvv

# yourName = input("Enter your name\n").lower();
# herName = input("Enput her name\n").lower();
#
# turuLovv = yourName + herName
# print(turuLovv)
#
# t = turuLovv.count('t')
# r = turuLovv.count('r')
# u= turuLovv.count('u')
# e= turuLovv.count('e')
# l= turuLovv.count('l')
# o= turuLovv.count('o')
# v= turuLovv.count('v')
#
# fchar = t + r + u + e
# lchar = l+o+v+e
#
# strLove = str(fchar)+str(lchar)
#
# lovep = int(strLove)
#
# if lovep<10 or lovep>90:
#     print("Your love is like coke and mentos")
# elif lovep>=40 and lovep<=50:
#     print("You are alright")
# else:
#     print(lovep);


# Final challange -> Tresure IsLand
print('''▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█▄░▄█░▄▄▀█░▄▄█░▄▄▀█░▄▄█░██░█░▄▄▀█░▄▄████▄██░▄▄█░██░▄▄▀█░▄▄▀█░▄▀
██░██░▀▀▄█░▄▄█░▀▀░█▄▄▀█░██░█░▀▀▄█░▄▄████░▄█▄▄▀█░██░▀▀░█░██░█░█░
██▄██▄█▄▄█▄▄▄█▄██▄█▄▄▄██▄▄▄█▄█▄▄█▄▄▄███▄▄▄█▄▄▄█▄▄█▄██▄█▄██▄█▄▄█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')
print('''     .-'"""'-.
      ,____|_______|____,
       '._____________.'  REACH FOR
           |.-- --.|      THE SKY!
           |(o) (o)|
          (|       |)
           |   U   |
 __        | .___. |    YOU'RE MY 
/|||       |       |     FAVORITE
||||       :       :      DEPUTY!
|  |/)      `.___.'
 \  /       __) (__
  \/\      /\ \ / /\
   \ \    /\ \ ^ / /\    THERE'S A
    \ \  / |  |0_/\_ \    SNAKE IN
     \ \/ /|  | \  /\ \    MY BOOT!
      \  / |  |0//\\ \ \
       \/  | /   \ |  \ \
           |/ .-. \|  / /
        .-'|-( ~ )-| / /   HI!
        \  |--`-'--|/ /   MY NAME'S WOODY!
         \ |       | /
          \|   |   |/
           |   |   |
           |   |   |     HOWDY PARDNER!
           |   |   |
           |   |   |
           |   |   |
           |___|___|     YEEEHAH COWBOY!
          `|---|---|'
          *|   |   |*
           |_._|_._|
          /'  /|\  '\    SOMEONE POISONED
     jgs /   /^ ^\   \    THE WATERHOLE!
        /__.'     `.__''')
print("Welcome to the treasure island")
print("Your mission is to find the tresure")
dir = input("You have teo choices, Left or right").lower();

if dir=="right":
    print("Game Over, You are inside the snake ialand")
elif dir=="left":
    c2 = input("We have lake in front of us, Swim or Wait for boat").lower()
    if c2=="swim":
        print("Corcodile eats hahahaha, Game over")
    elif c2=="wait":
        c3 = input("Choose Door in front of you, red, yellow, green")
        if c3=="red":
            print("Lava, game over")
        elif c3=="green":
            print("Plant monster, game over")
        elif c3=="yellow":
            print("You won!, Inside the heven")

