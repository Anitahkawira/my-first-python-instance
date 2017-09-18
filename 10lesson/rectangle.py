#def area_Rectangle(base,height):
    #int_base = int(base)
    #int_height = int(height)
    #area = int_base * int_height
    #return area
#base = input("what is the base of the rectangle?")
#height = input("what is the height ot the rectangle?")
#area = area_Rectangle(base,height)
#print (area)

#class Rectangle():
    #def area(self,base,height):
        #int_base = int(base)
        #int_height = int(base)
        #area = int_base * int_height
        #return area
#base = input("what is the base of the rectangle?")
#height = input("what is the height of the rectangle?")
#rectangle = Rectangle()
#area = rectangle.area(base,height)
#print(area)

#class Rectangle():
    #def __init__(self,base,height):
        #self.base = int(base)
        #.height = int(height)
    #def area(self):
        #return self.base * self.height
#base = input("what is the base of the rectangle?")
#height = input("what is the height of the rectangle?")
#rectangle = Rectangle(base,height)
#area = rectangle.area()
#print(area)

class Rectangle():
    def __init__(self,base,height):
        self.base = int(base)
        self.height =int(height)
    def area(self):
        return self.base * self.height
    def perimeter(self):
        return 2 * self.base + self.height
base = input("what is the base of the rectangle?")
height = input("what is the base of the rectangle?")
rectangle = Rectangle(base,height)
print("The area of the rectangle is {} and its perimeter {}".format(rectangle.area(),rectangle.perimeter()))