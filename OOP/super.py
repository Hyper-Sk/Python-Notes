class Cars:
    def __init__(self,type):
        self.type = type 
    @staticmethod
    def startCar():
        print('Started')
    @staticmethod
    def stopCar():
        print('Stopped')


class ToyotaCars(Cars):

    def __init__(self,name,type):
        self.name = name

        # super method is used to used to access method of parent class 
        
        super().__init__(type)
        # super().startCar()
        # super().stopCar()


fortuner = ToyotaCars('Fortuner','Diesel')

fortuner.startCar()
print(fortuner.type)

