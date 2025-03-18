mySet = {'apple','grapes','banana'}

secondSet = {'mango','orange'}

# merging two set using update 
mySet.update(secondSet)
print(mySet)


# merging set with list and it still works
myList = ['stawberry','gouva','chiko']
mySet.update(myList)

print(mySet)

print("___('_')___")

# The union() method returns a new set with all items from both sets:
set1 = {'apple','grapes','banana'}
set2 = {1,2,3,4,5}

set3 = set1.union(set2)
print(set3)

# keep only the duplicate item in the set 
# intersection_update() compare and keep duplicate items 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

print("(^_^)")

# intersection() compare and keep duplicate items and return new array
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}

c = a.intersection(b)
print(c)

print('("_")')

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

e = {"apple", "banana", "cherry"}
f = {"google", "microsoft", "apple"}

e.symmetric_difference_update(f)
print(e)

print('(*_*)')

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
# here True is considired the same value set.

l = {"apple", "banana", "cherry", True}
m = {"google", "microsoft", "apple", 1}

o = l.symmetric_difference(m)
print(o)

