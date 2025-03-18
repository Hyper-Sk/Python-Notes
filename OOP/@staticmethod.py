class myClass:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    
    # staticmethod work at class level 
    # in static method we can create method without parameter 
    @staticmethod #decorator 
    def greetings():
        print("Welcome back student ^-^ ")

student = myClass('salman',6)

student.greetings()

