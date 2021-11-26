# class User:
#     pass
#
#
# james = User()
# james.age = 22
# james.id = "001"
# james.userName = "james221"
# henry = User()
# henry.age = 18
# henry.id = "002"
# henry.userName = "Henryviii"

class User:

    def __init__(self, userId, userName):
        # these lines of code are triggered each time an object is built.
        # self is the actual object itself
        self.userId = userId
        self.userName = userName
        self.followers = 0
        self.following = 0
        # ^ this is a default value


    def changeUserName(self, newName):
        self.userName = newName

    def follow(self, user):
        user.followers += 1
        self.following += 1


user22 = User("022", "James221")
user22.changeUserName("BigMan221")
user21 = User("21", "LittleMan221")
user21.follow(user22)

print(user21.followers)
print(user21.following)

print(user22.followers)
print(user22.following)
