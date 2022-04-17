#  DataType ->
#  String -> Array or collection of char
#
# message = "Hello"[0];
# print(message);
#As we are declearing the variable we can do this to tell compiler that this variable must be of some type
name:str
age:int
height:float
can_vote:bool

# def is_votable(canVote:bool)->bool: // this tells compiler that it take bool type in nd give bool type output

# and in future it will tell us hint that it is a type of variable so use this
# # Integer ->
#
# age = 20;
# print(age);
#
# # boolean ->
# canVote = True;
# print(canVote);
#
# # floate ->
# pi = 3.14;
# print(pi);
#
# # type
# print(type(pi));
#
# # typecast
# age = "20";
# money = 30;
# print(type(age));
# print(type(money));
#
# age2 = int(age);
# print(type(age2))
# print(age2 + money);
#
# print(70 + float("60.2"));
#
#
# # challage
# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: \n")
# # 🚨 Don't change the code above 👆
#
# ####################################
# #Write your code below this line 👇
# d1 = str(two_digit_number[0]);
# d2 = str(two_digit_number[1]);
#
# res = int(d1) + int(d2);
# print(res);
#
#
# # operatoer
#
# # + - * /
#
# print(2 + 2)
# print(2**3); # 2 powers three
#
# # Bodmas ka brother Pemdas
# # ()
# # **
# #  * /
# # + -
#
# # Note -> Compiler read top to bottom left to right
#
# print(3 * 3 + 3 / 3 - 1);


# bmi
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# bmi = float(weight) /float(height)**2;
# print(bmi);

# remainDays
# 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# total_time = 90;
#
# curr_age = int(age);
# remainTime = (total_time - curr_age);
# totalDaysRemain = str(remainTime * 365);
# totalWeeks = str(remainTime * 52);
# totalMonths = str(remainTime * 12);
#
# print("You have " + totalDaysRemain + " days, " + totalWeeks + " weeks, and " + totalMonths + " months left.")
# or
# and now we cant have to type cast it
# print(f"You have {totalDaysRemain} days, {totalWeeks} weeks, and {totalMonths} months left.")

# round off

# number = round(8/3,4);
# print(number);
# # or
# number2 = (8//2);
# print(number2)
#
# # we cant always type case it so we use
# # fstring
#
# name = "priyansh";
# age = 20;
# cgpa = 8.14;
#
# print(f"naam {name} uamar {age} cgpa {cgpa} placed");

# challange -> bill calculator

# bill123 = input("What's the total bill guys? $");
# tip123 = input("What percent tip you wanna give? 10 12 15 ");
# peoples123 = input("How many people you are? ");
#
# bill = float(bill123);
# tip = int(tip123);
# people = int(tip123);
#
# billTotal = tip/100*bill + bill;
# total_after_tip = bill + billTotal;
# print(f"Sir your total after bill is {total_after_tip}");
# individual_cost = total_after_tip/people;
# finalAmount = "{:.2f".format(individual_cost);
# print(round(finalAmount,2));