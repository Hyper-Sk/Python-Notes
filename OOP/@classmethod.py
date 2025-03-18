# @static method can't access or modify class state 


# @class method is a bond to the class and receive the class as an implicit first argument 

# with the help of @classmethod we can access and modify class level state 

# example with @classmethod 
class myClass:
    brandName = 'toyata'

    @classmethod
    def changeBName(cls,name):
        cls.brandName = name


person1 = myClass()

person1.changeBName('mercedez')
print(person1.brandName)

print(" - - - - - - - -")


# example with ClassName : - 

class Car:
    brandName = 'anonymous'

    
    def changeBName(self,name):
        Car.brandName = name


car1 = myClass()

car1.changeBName('Bentley')
print(car1.brandName)

print(" - - - - - - - -")

# example with class chaning 

class Grocery:
    itemName = 'anonymous'

    
    def changeGName(self,name):
        self.__class__.itemName = name

grcry = Grocery()

grcry.changeGName('lady Finger')
print(grcry.itemName)

print(" - - - - - - - -")
