class Member:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    


result = Member('alex',55)
result.age = 33
print(result.age) #now the age is 33

