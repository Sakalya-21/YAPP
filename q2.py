class Circle:

    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        print("Perimeter of Circle with radius {} is {}.".format(self.radius,2*self.radius*3.14))
    
    def area(self):
        print("Area of Circle with radius {} is {}.".format(self.radius,self.radius*self.radius*3.14))


if __name__=='__main__':

    print(f"Sakalya Mitra:20MIM10056\n")
    obj1 = Circle(5)
    obj1.perimeter()
    obj1.area()
