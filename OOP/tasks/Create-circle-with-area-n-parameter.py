class Circle:


    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    


circle = Circle(6)
print("Area of Circle :",circle.area())
print("Parimeter of Circle : ",circle.perimeter())