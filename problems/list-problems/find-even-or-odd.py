
def find_even(input_list):
    new_list = []
    for x in input_list:
        if x % 2 == 0:
            new_list.append(x)

    return new_list

print(find_even([1,2,3,4,5,6,7]))


def find_odd(input_list):
    new_list = []
    for x in input_list:
        if x % 2 == 1:
            new_list.append(x)

    return new_list

print(find_odd([1,2,3,4,5,6,7]))