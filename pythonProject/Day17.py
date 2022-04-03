class User:
    def __init__(self,user_id,name):
        self.id = user_id
        self.name = name
        self.followers = 0 # This is a default value so we dont have to repeat it
        self.following = 0

    def follow(self,user):
        user.followers +=1
        self.following+=1

user_1 = User(1,"Priyansh sharma")
user_2 = User(2,"Shreyansh sharma")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)



# user_1.id = 1
# user_1.name = "Priyansh Sharma"
#
# user_2 = User()
# user_2.id = 2
# user_2.name = "Shreyansh Sharma"
# -----------------------Constructor--------------------------------------------
# But for everytime we will not be doing this
# so we can initlize the fields when we create a object using conatrucor
# We use __init__(self) for initlize the attributes-> self is our boject and other parameters are fielsds
# -----------------------Method--------------------------------------
# When a function declear inside the class it is a method
# first peremeter is self, this is what our object does