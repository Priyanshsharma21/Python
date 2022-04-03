# Inheritance -> It is a conceot in which a class can inherit all
# the information from other class(code resuablity you know

# How to deo it

# ------------------------------------------------
# class fish(Animal):
#     def __init__(self):
#         super.__init__()
        # This means we inherit all property of animal and
        # super is used to point toward all the value we initlizr inside the
        # parent class so we dont have to initlize all the things again
# ---------------------------------------------------------------------

class Fish :
    def __init__(self):
        self.number_of_eyes= 2

    def breadth(self):
        print("Inhale Exhale")

class Nemo(Fish): # Inherit Fish class
    def __init__(self):
        super().__init__() # can use all the method and attributed of Fish now
        self.speed_of = 200 # can all new ones too

    def breadth(self): # method overriding
        super().breadth()
        print("Inside the water")

    def swim(self):
        print("Swiming baby")


nemo = Nemo()
nemo.breadth()