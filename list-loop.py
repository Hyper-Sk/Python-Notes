# looping techniques :-

x = [1,2,34,333]
for i in x:
    print(i)
print("---------------")


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print("---------------")


myList = ['orange','grapes','banana','mango']

# newlist = [expression for item in iterable if condition == True]
myFruits = [x for x in myList if x == 'orange']

for x in myList:
   if x == 'orange':
      print([x])


print(myFruits)

print("---------------")
