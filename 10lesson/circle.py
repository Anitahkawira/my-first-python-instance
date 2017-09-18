import math
class Circle():
    def __init__(self,radius):
        self.radius =int(radius)
    def area(self):
        return math.pi * (self.radius **2)
    def perimeter(self):
        return 2 * math.pi * (self.radius)
radius = input("what is the radius of the circle?")
circle = Circle(radius)
print("the area of the circle is {} and its perimeter {}".format (circle.area(),circle.perimeter()))
    
    
    