# here we are converting tuple to list for changing its values and then changing back to tuple.

mytuple = ("apple", "banana", "cherry")
myList = list(mytuple)
myList[1] = "kiwi"
mytuple = tuple(myList)
print(mytuple)

print("---------------->")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)