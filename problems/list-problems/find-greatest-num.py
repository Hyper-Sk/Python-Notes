
def find_max(input_list):
    st = 0
    for x in input_list:
        if st < x:
            st = x
    return st

print(find_max([1,2,3,4,5,2,7,8,19,22,15]))