# Backend -> Client server Databases
# Client part where user intrace
# Server strong computer is on 24*7
# Database where we store all our data
# ----------------------------------------------------------

# Working
# User type google.com request for webpage
# google server response it and send response as html css js

# ----------------------------------------------------------

# Library -> SOmething that we call upon to do something
# Framework -> Framework call us

# ----------------------------------------------------------
# How to start server
# 1. $env:FLASK_APP="hello.py"
# 2. flask run

# -------------------------------------------------------
# nested function
import time


def outer():
    print("I am outer")

    def inner():
        print("I am inner")

    # this inner can only be used inside the outer and have lexical scope of outer

# we can return function and can store it inside the function


def outers():
    print("I am outer")

    def inners():
        print("I am inner")

    return inners

innerval = outers()
# now we can access inner also
innerval()

# 1. Functions can have functionality i/p and o/p
# 2. functions are first class objects and can pass as args
# 3. can be nested
# 4. can reurned

## Decoraroe
# def decorator_function(function):
#     def wapper_function():
#         function()
#     return wapper_function

def delay_deco(function):
    def wapper_function():
        time.sleep(2)
        # do some thing before function
        function()
        # do some thing afer function

    return wapper_function

def say_hi():
    print("Hello")

@delay_deco
def say_double_se_hello():
    print("Hey")

say_double_se_hello()
delayed_func = delay_deco(say_hi)
delayed_func()

import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()