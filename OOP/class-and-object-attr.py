class Person:
    # below var's we call class properties 
    # properties contains data --->

    # name = 'john'
    # age = 22


    def __init__(self,name,age):
        # below var's we call object properties or instance properties --->
        self.name = name 
        self.age = 33



# creation of object 
myObject1 = Person("Karan",22)
myObject2 = Person("salman",21)
myObject3 = Person('shahrukh',33)


print(myObject1)
print(myObject1.name)
print(myObject2.name)
print(myObject3.name)