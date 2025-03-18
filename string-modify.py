
# modifing string  ---> 

a = "Hello, World! "
print(a.lower())

b = "Hello, World!"
print(b.upper())

# it will remove whitespace from starting and ending

text1 = 'PYTHON IS AWESOME!'
print(text1.isupper())
#> True

text2 = 'PYTHON IS AWESOME!'
print(text2.islower())

text3 = '5664dffdgf'

print(text3.isnumeric()) #False only nums
print(text3.isalpha()) #True only alpha
print(text3.isalnum()) #True both



c = "          Hello, World!"
print(c.strip())


# replacing string --->

d = "Hello, World!"
print(d.replace("H", "J"))


# spliting string ----> 

y = "Hello World!"

print(y.split())

print(type(y.split(" ")))
