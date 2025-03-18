def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    x = 0
    for i in input_string:
        if i in vowels:
            x += 1
    return print(x)

count_vowels('hello world')

    