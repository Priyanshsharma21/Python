def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


addition = add(10, 20,30, 40, 30, 39, 29)
print(addition)

def calculatoe(n,**kwargs):
    n += kwargs["add"]
    n*= kwargs["mult"]
    print(n)


calculatoe(2,add=3, mult=5)

class Car:
    def __init__(self,**kwargs):
        self.door = kwargs["doors"]
        self.speed = kwargs.get("speed")
        # we use get because if we dont pass speed in constructor then it take it as null
        # otherwise it will through error

car = Car(doors=4)
print(car.speed)

# so similary in tkinter we have class label which is initlize with **kwargs
# thats why we didnt see any methods