class myClass:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    # here we are creating methods to use 
    def getAvgMarks(self):
        sum = 0 
        for i in self.marks:
            sum += i

        totalSubjects = 5
        return sum/totalSubjects
    
    def getTotal(self):
        sum = 0 
        for i in self.marks:
            sum += i
        return sum


# creation of object 
person = myClass('salman',[42,65,80,38,89])


print("your Name is",person.name , " and average marks is : " , person.getAvgMarks())

print("your Name is ", person.name,"and your total marks is : ",person.getTotal())