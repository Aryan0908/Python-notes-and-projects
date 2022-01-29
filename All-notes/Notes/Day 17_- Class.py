# Creating a class
class User:
    # Passing an empty class or function
    pass

print(User)

class User:
    # A constructor fuction will help us to give attributs value to out class
    """
    __int__(self) is a fuction that helps in giving initial value to our class attributes. After the self parameter
     we can add as much parameters as we want
    """
    def __init__(self, user_id, username):
        self.id = user_id  # here .id is the attribute/ variable and is equal to the user_id parameter
        self.name = username
        self.followers = 0
        self.following = 0

    # Introducing a method/function
    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "Aryan")
user_2 = User("002", "Vivek")
user_1.follow(user_2)


print(user_1.followers)
print(user_2.followers)
print(user_1.following)
print(user_2.following)