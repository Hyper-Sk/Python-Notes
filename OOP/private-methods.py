class myClass:
    def __init__(self,name):
        self.name = name

    def __hello(self):
        print('Hello',self.name, "^_^")

    def welcome(self):
        self.__hello()


person = myClass('robot')
# person.__hello() # you can't call private funtion as an instance --->
person.welcome()

