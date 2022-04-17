# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged = False
#
#
# def login_decorator(function):
#     def wrapper(*args):
#         if args[0].is_logged:
#             function(args[0])
#     return wrapper
#
#
# @login_decorator
# def message(user):
#     print(f"You are loged in, welcome {user.name}")
#
#
# user = User("priyansh sharma")
# user.is_logged == True
# message(user)

def is_logged_in(fn):
    def wrapper(*args):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"returned result is {result}")
    return wrapper

@is_logged_in
def a_func(a,b,c):
    return a*b/c

a_func(1,2,3)

