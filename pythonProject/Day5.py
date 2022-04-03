import random

# Loop
# i inxed will loop through all the value in list and print each of them
# ------------------------intro-----------------------
# fruits = ["Apple","peach","banana"]
#
# for i in fruits:
#     print(i)


# ex->1

# student = input("Enter your height")
# studentList = student.split(" ")
# for i in range(0,len(studentList)):
#     studentList[i] = int(studentList[i])
# print(studentList)
# ------------------height average------------------------
# ------we have len() for count and sum() for sum
# sum = 0
# count = 0
#
# for i in studentList:
#     sum+=i
#     count+=1
#
# average = round(sum / count)
# print(average)
# --------------------------chal1-----------------
# 2. print heighest, we have max and min function
# heighest = studentList[0]
# for i in studentList:
#     if i>heighest:
#         heighest=i
# print(heighest)
# # or
# print(max(studentList))
# -----------------------------------
# 3. Range function

# for i in range(2,100):
#     if i%2==0:
#         print(i)
# or
# for i in range(2,100,2):
#     print(i)


# -----------------chal4-------------

# sum = 0
# for i in range(0,101,2):
#     sum +=i
# print(sum)

# ------------fizzBuzz baby------------------

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz Baby")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

# --------------password Generator---------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letterUWant = int(input("How many letters you want me to include:\n"))
numbersUWant = int(input("How many numbers you want me to include:\n"))
symbolesUWant = int(input("How many symboles you want me to include:\n"))
# easy version
# password = ""
# for i in range(0,letterUWant+1):
#     password+=random.choice(letters)
# for i in range(0,numbersUWant):
#     password += random.choice(numbers)
# for i in range(0,symbolesUWant):
#     password+=random.choice(symbols)
#
# print(str(password))

# hard version
password = []

for i in range(0, letterUWant + 1):
    password.append(random.choice(letters))
for i in range(0, numbersUWant + 1):
    password.append(random.choice(numbers))
for i in range(0, symbolesUWant + 1):
    password.append(random.choice(symbols))

# print(password)
random.shuffle(password)
# print(password)

auth=""
for i in password:
    auth+=i

print(f"Your unHackable password is =  {auth}")
