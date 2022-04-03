# --------------------------------------Theory----------------------------------------------
# why oops
# Till now we are doing a procedure programing
# On hitting a function from top to bottom our code reaches to function whereever it is
# When we have some project with more functionality we can break it on servel modules and our team can work on it
# you cant be a one men army in programming
# In oops we can divide our task in serval parts and
# one can manage tham all
# Its object oriented programming

# How to implement it
# In oops we have to model real world objects
# We have to think or
# 1. what object has (attributes) variable
# 2. What object does(can do) (methods) function
# 3. Variables and function are attach to a particula r model thats why
# it is called method and attributes

# oops ---combining--> data and functionality in same thing
# we can generate same type of object which follow same bluprint called class


# car = CarBluprint() # Creating a car object from a car bluprint
# audiModel1 = Car() // audimodel1 has car object
# --------------------Turtle-------------------------------
# we will be using a bluprint that someone else created called turtle
# To construct a object we need Class()
# Here we have imported a Turtle module and inside a turtle module we have a class so we construct a object of it
# by -> tt = turtle.Turtle()
# we can access attributes in it by obj.attribute_name
# we access method by obj.method()
# --------------------------------Packages--------------------------------
# This is more than a module , it cointain bunanch if files kept together
# ---------------------------------------------------------------------------------------------
# import turtle
# import turtle
# from turtle import Turtle,Screen
# timmy = Turtle()
#
# my_sreeen = Screen()
# print(my_sreeen.canvheight)
# timmy.shape("turtle")
# timmy.color("red")
# turtle.forward(85.00)
# turtle.circle(25)
# turtle.write("Priyansh",True,align="center")
#
# my_sreeen.exitonclick()
# --------------------------------------------------------------
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Captain name", "Team", "Home", "Trophys"]
table.add_row(["Virat Kholi", "RCB", "Banglore", 0])
table.add_row(["Rohit", "MI", "RCB", 5])
table.add_row(["Shreyash", "KKR", "RCB", 2])
table.add_row(["MS Dhoni", "CSK", "RCB", 4])
table.add_row(["Hardik Pandya", "GT", "RCB", 0])
table.add_row(["Rishab", "RCB", "DC", 0])
table.add_row(["Shami", "KXIP", "Panjab", 0])
table.add_row(["Williomson", "SRH", "Hydrabad", 2])
table.align="r"

# print(table)
print(table.get_string(sortby="Trophys"))














