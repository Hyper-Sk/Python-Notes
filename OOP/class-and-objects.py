# class is the blueprint of object
# with class keyword we create class  
class Person:

    # Person properties 
    name = 'john'
    age = 22


# creating object from the class or can also call this an instance.
myObject1 = Person()
myObject2 = Person()
myObject3 = Person()

# every object create the same name and age if it class a class-attribute

print(myObject1)
print(Person.name)
print(myObject2.name)
print(myObject3.name)