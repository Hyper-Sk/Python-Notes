# startwith and endwith are case-sensitive... \
strg = 'Python'
isP = strg.startswith('P')
print(isP)
#> True

isP = strg.endswith('n')
print(isP)
#> True


mylist = ['text','Jane', 'Jack','Ashley']

for i in mylist:
    if i.startswith('J'):
        print(i)