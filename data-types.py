# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# a = "Hello World"	str	
# a = 20	int	
# a = 20.5	float	
# a = 1j	complex	


# a = ["apple", "banana", "cherry"]	list	
# a = ("apple", "banana", "cherry")	tuple	
# a = range(6)	range	
# a = {"name" : "John", "age" : 36}	dict	
# a = {"apple", "banana", "cherry"}	set	
# a = frozenset({"apple", "banana", "cherry"})	frozenset	
# a = True	bool	
# a = b"Hello"	bytes	
# a = bytearray(5)	bytearray	
# a = memoryview(bytes(5))	memoryview	
# a = None	NoneType

# exercise ----> 

# string | ordered Indexed
char = 'hello world'
print(type(char))

# type method is used to check the data type of the data type(data)

# integer | ordered Indexed 
integer = 25
print(integer)

#float 
decimal = 0.333
print(type(decimal))

# bool
isStudent = True
print(isStudent)

#list | ordered Indexed | can be access index item 
lst = ['apple',33,0.45]
print(lst)

#tuple | ordered Indexed | can be access index items | slow compare to set
tpl = ('apple',3,True, 5.55)
print(tpl)

#range 
count = range(2)
print(count)


#dictionary | unordered | 
dictry = dict(name='john',age=36, percentage=8.5)

dict2 = {
    "fruit":"banana",
}
print(dictry)

#set | Unordred | unique values |  use hash techniques | Fast | can't access index item
dataset =  {'apple',20,0.4,True,'apple'} # set(('apple',20,0.4,True,'apple')) 
print(dataset)

newList = list(dataset)
print(newList)

#frozen-set 
fznset = frozenset(('orange',20,0.4,True))
# print(fznset)

newList2 = list(fznset)
newList2[1] = 333333333
print(newList2)

