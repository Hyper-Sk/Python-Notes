# @property method convert return funtion into attribute(variable) whenever single state changes it reflect the change in attribute(variable)

# we can call it like an attribute(varaible)

# example 


class Student:

    def __init__(self,english,math,science):
        self.english = english
        self.math = math
        self.science = science

    @property
    def percentage(self):
        return str((self.english + self.math + self.science) / 3) + '%'




stu = Student(66,44,55)
print(stu.percentage)

stu.math = 38
print(stu.percentage)

