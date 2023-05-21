class User():
            def __init__(self, birthday):
                self.__birthday = birthday

user = User(1997)
print(user.__birthday) #报错
print(user._User__birthday) #正常a