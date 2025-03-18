class myClass:

    # default constructor, this constructor is already created by class 
    def __init__(self):
        pass

    # in both inits constrcut below init assums to be executed because its match paramaters 


    # this init function directly executes when ever object is created
    def __init__(self,yourname,yourage):
        print('adding user information')
        self.name = yourname
        self.age = yourage
    

z = myClass("john",21)
print(z.age)
print(z.name)