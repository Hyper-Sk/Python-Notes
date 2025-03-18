# sort() it will modify the orignal list..

num = [3,4,5,2,5,1]
num.sort()
print(num)

# sorted() it won't modify the orignal list..
num2 = [3,5,2,35,1]
sorted_num = sorted(num2)

print(sorted_num)


strg = 'hello world'

newset = set(strg)
print(newset)