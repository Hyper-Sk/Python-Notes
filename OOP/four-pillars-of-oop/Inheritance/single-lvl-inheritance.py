class NissanCars:
    brandName = "Nissan"
    yearStarted = 1977

    @staticmethod
    def startCar():
        print('Car Started = = = > ')
    
    @staticmethod
    def stopCar():
        print('Car is Stopped < = >')



class NissarGTR(NissanCars):
    colors = ['black','white']

    @staticmethod
    def type():
        print('Diseal Engine')



nissarGTR = NissarGTR()
nissarGTR.type()
print(nissarGTR.colors)


#inheritance :

nissarGTR.startCar() 
print('| = = = = = = = = = = = = |')
nissarGTR.stopCar()