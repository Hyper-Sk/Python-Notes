class ToyotaCars:
    brandName = "Toyota INC"

    def startCar(self):
        print('Car Started = = >')

    def stopCar(self):
        print('Car Stopped')

    
class Fortuner(ToyotaCars):
    colors = ['white','black']

    def type(self):
        print('Petrol Engine')
    

class Supra(Fortuner):
    colors = ['yellow','orange']

    def type(self):
        print('Diesel Engine')



supra = Supra()
fortuner = Fortuner()


fortuner.type() #petrol
supra.type() #diesel
