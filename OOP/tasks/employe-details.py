# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("Role is : ",self.role)
#         print("Department is : ",self.dept)
#         print("Salary is : ",self.salary)


# employee = Employee('Frontend Developer','IT',"25,000")

# employee.showDetails()


# example with inheritance : -  ---> 

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role is : ",self.role)
        print("Department is : ",self.dept)
        print("Salary is : ",self.salary)
       

class BackEndDev(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Backend Developer",'IT','40,000')


backend = BackEndDev('salman Khan',35)

backend.showDetails()

