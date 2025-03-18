class BMWCars:
    brandName = "B-M-W cars"

    @staticmethod
    def startCar():
        print('Car Started - - - - - >')
    @staticmethod
    def stopCar():
        print('Stop Car')


    
class A4(BMWCars):
    colors = ['white','orange']

    @staticmethod
    def type():
        print('Petrol Engine')



class A5(BMWCars):
    colors = ['silver','matt black']
    @staticmethod
    def type():
        print('Hybrid and Petrol Engine')


a4 = A4()
a5 = A5()


a4.startCar()
a4.type()
print(a4.colors)

print("- - - - - - ")

a5.startCar()
a5.type()
print(a5.colors)
