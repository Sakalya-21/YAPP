class Address:

    number = None
    StreetName = None
    
    def __init__(self, num, stype):
        self.number = num
        self.StreetName = stype


if __name__=='__main__':
    
    print("Sakalya Mitra:20MIM10056")
    print("\n")
    
    obj = Address(224,"Mahamaya Temple Road")
    print("The Address is with Number: {} and Street Name: {}.".format(obj.number,obj.StreetName))