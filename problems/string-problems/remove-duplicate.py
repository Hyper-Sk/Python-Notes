# def remove_duplicates(input_string):
#     x = "".join(sorted(set(input_string), key=input_string.index))
#     return print(x)

# remove_duplicates('hello world')


def remove_duplicates(input_string):
    result = ''
    for st in input_string:
        if st in result:
            pass
        else:
            result = result + st
    return print(result)
           

remove_duplicates('hello world')
    