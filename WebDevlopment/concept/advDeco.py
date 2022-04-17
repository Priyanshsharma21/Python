class User:
    def __init__(self, name, sername):
        self.name = name
        self.sername = sername
        self.is_logged = False



def is_authinticate(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged == True:
            function(args[0])

    return wrapper


@is_authinticate
def create_blog_post(user):
    print(f"Blog post created for {user.name}, {user.sername}")

new_user = User("Priyansh sharma", "sharmaji")
new_user.is_logged = True
create_blog_post(new_user)

