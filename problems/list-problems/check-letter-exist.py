# list1= ['orange','grapes','avacado','mango','apple']
# list2 = []
# input1 = input()

# for x in list1:
#     if input1 in x:
#         list2.append(x)
# print(list2)


# short form 
list3= ['orange','grapes','avacado','mango','apple']
input2 = input('type something : ')
list4 = [x for x in list3 if input2 in x]

print(list4)
