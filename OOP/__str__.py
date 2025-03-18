class myClass:
    def __init__(self,name,year):
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.name}({self.year})"

person = myClass("jerry",2024)

# here we are not calling name or year we are just calling person 
print(person)