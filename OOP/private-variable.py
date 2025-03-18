class myClass: 
    __bankName= "swiz bank"
    def __init__(self,password,account):
        # by giving double underscore to the variable will be declare as private variable 
        self.__password = password
        self.account = account

    def getPassword(self):
        print(self.__password)
        
    

result = myClass("abc123","223344")

print(result.account)
# you can't access password coz it is private.
# print(result.__password)

#however you can get pass by calling other methods or function. 
result.getPassword()