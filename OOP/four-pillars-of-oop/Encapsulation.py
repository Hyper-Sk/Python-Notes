# Encapsulation :

# Wrapping data and function into a single unit (object). 


class myClass:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def greeting(self):
        print('welcome back...')

# creating an object 
# which contains funtions and data 
# so wrapping data and funtion is encapsulation.
        
person = myClass('salman',33)
person.greeting()





