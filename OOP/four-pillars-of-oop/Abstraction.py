# Abstration : 

# hiding the implementation code and data details of a class and only showing the essential features to the users. 

# in simple words not showing unnessesary things from class is abstraction 

# example : - 

class Bike:
    def __init__(self):
        self.acc = False
        self.backBreak = False
        self.clutchLvr = False

    def startBike(self):
        self.clutchLvr = True
        self.acc = True
        print('Bike started ....')


bike = Bike()

# here user can only see print statement "bike started ...".
# other code is hidden and this is how abstraction look like.
bike.startBike()




    