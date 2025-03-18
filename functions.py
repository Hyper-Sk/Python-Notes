# function with single parameter 
def my_function(fname):
    print(fname + 'khan')

my_function('feroz')
my_function('amir')
my_function('salman')


# function with double parameter 

def hello(fname,lname):
    print(fname+'~'+lname)

hello('salman','khan')


# more than 3 arguments in parameter 

def multiple(*names):
    print(type(names))
    print('The person name : - ' + names[1])

multiple("shazim","sameer","saif","raheem")




# function with return 

def func(a,b):
    x = a+b 
    return 0
func = func(3,5)

if func:
    print('value is True !')
else:
    print('value is False !')