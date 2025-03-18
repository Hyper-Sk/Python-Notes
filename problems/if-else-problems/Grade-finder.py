marks = int(input('Enter any marks : '))


if(marks >= 90):
    print('Your Grade : A+')
elif(marks >= 80 and marks < 90):
    print('Your Grade : A')

elif(marks >= 70 and marks < 80):
    print('Your Grade : B+')

elif(marks >= 60 and marks < 70):
    print('Your Grade : B')

elif(marks >= 50 and marks < 60):
    print('Your Grade : C')

elif(marks >= 35 and marks < 50):
    print('Your Grade : D')

elif(marks >= 30 and marks < 35):
    print('Your Failed')
else:
    print('Please Enter Valid Marks 10 - 100')
