# When the same operator is allowed to have different meaning according to the context is called polymorphism. also called operator overloading.

# so when use operators it rapidly call dunder funtions 

# every operator has there own dunder funtion 

# example with string :
class Items:

    def __init__(self,item):
        self.item = item

    def __add__(self,item2):
        return self.item + item2.item
        

item1 = Items('tea')
item2 = Items('coffie')

print(item1 + item2)


class Number:
    def __init__(self,number):
        self.number = number

    def __add__(self,number2):
        return self.number + number2.number
    
    def __sub__(self,number2):
        return self.number - number2.number
    
    def __gt__(self,number2):
        return self.number > number2.number
    
    def __lt__(self,number2):
        return self.number < number2.number
    
number1 = Number(22)
number2 = Number(11)

print(number1 + number2)
print(number1 - number2)
print(number1 > number2)
print(number1 < number2)