
myDict = {
    'name':'salman',
    'age':19,
    'height':5.3,
    'weight': 70,
    'isMale':True,
    'skills':['web designer','web developer','graphic designer']
}

# get method :
# gets the value from the key 
name = myDict.get('name')
print(name)

print('-------------------')
# keys() method :
# get all the key from the dict

keys = myDict.keys()
print(keys)

print('-------------------')


values = myDict.values()
print(values)

print('-------------------')


# the item() method will print all key and values pair 
items = myDict.items()
print(items)

