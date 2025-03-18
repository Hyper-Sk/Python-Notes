# remove tuple items by converting into list

myTuple = ("apple", "banana", "cherry")
myList = list(myTuple)
myList.remove("apple")
myTuple = tuple(myList)


print(" <o^o> ")
print(myTuple)
print(" < - ^ - > ")