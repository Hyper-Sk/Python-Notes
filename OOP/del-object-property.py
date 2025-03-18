class Member:
    def __init__(self,name,age):
        self.name = name
        self.age = age


result = Member('gorge',33)

del result.age
print(result.age) # will show error says object has no attribute age.
