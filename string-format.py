# age = 20
# txt = "My name is shiva, I age is " + age
# print(txt)

# above code will through error 
# coz you can't concat string with integer 


# try this :

age1 = 21
age2 = 22
age3 = 23


msg = "My name is shiva, and I am {}"
print(msg.format(age1,age2))

# more examples 

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# specifice where you want data by using index 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))