# find factorial of any number :- 

def factorial(input_num):
    num = 1
    for x in range(input_num):
        num = num * (x + 1)
    return num

print(factorial(7))