class Rectangle:
    
    def __init__(self,length,width):
        self.l = length
        self.w = width

    def perimeter(self):
        print("Perimeter of Rectangle is {}.".format(2*(self.l+ self.w)))
    
    def area(self):
        print("Area of Rectangle is {}.".format(self.l*self.w))


if __name__=='__main__':

    print("Sakalya Mitra:20MIM10056")
    print("\n")
    obj1 = Rectangle(5,4)
    print("Length of Rectangle: ", obj1.l)
    print("Width of Rectangle: ", obj1.w)
    obj1.perimeter()
    obj1.area()