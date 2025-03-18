class Member:
    def __init__(self,name,age):
        self.name = name
        self.age = age


result = Member('alex',21)
del result
print(result.name) # shows error says object is not defined.
