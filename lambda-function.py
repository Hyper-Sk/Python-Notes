# lamda function : 
# lambda function take multiple arguments and (returns) a single expression.

# single parameter function 
x = lambda a : a + 10
print(x(5))

# double argument function 
y = lambda a,b : a + b
print(y(10,3))



# advanced example : 

def func(num):
    return lambda a : a * num
argu = func(5)
print(argu(11))