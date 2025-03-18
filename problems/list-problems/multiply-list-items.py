# multiply list items

def multiplier(input_list):
    mul = 1
    for x in input_list:
        mul *= x
    return mul;

print(multiplier([1,2,3,4]))