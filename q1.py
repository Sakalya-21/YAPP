class Complex:
     
    # Constructor to accept real and imaginary part
    def __init__(self, tempReal, tempImaginary):  
        self.real = tempReal;
        self.imaginary = tempImaginary;
 
    # Defining add complex number method
    def addComp(self, C1, C2):
 
        # creating temporary variable
        temp=Complex(0, 0)
  
        # adding real part of complex numbers
        temp.real = C1.real + C2.real;
  
        # adding Imaginary part of complex numbers
        temp.imaginary = C1.imaginary + C2.imaginary;
  
        # returning the sum
        return temp;
    
    def subComp(self,C1,C2):

        # creating temporary variable
        temp=Complex(0, 0)
  
        # subtracting real part of complex numbers
        temp.real = C1.real - C2.real;
  
        # subtracting Imaginary part of complex numbers
        temp.imaginary = C1.imaginary - C2.imaginary;
  
        # returning the result
        return temp;
    
    def mulComp(self,C1,C2):

        # creating temporary variable
        temp=Complex(0, 0)
  
        # multiplying real part of complex numbers
        temp.real = (C1.real*C2.real)-(C1.imaginary*C2.imaginary);
  
        # multiplying Imaginary part of complex numbers
        temp.imaginary = (C1.real*C2.imaginary)+(C2.real*C1.imaginary);
  
        # returning the result
        return temp;
    
    def checkEqual(self,C1,C2):

        if((C1.real==C2.real) and (C1.imaginary==C2.imaginary)):
            return True
        else: return False
    
    def checkGreater(self,C1,C2):
        if((C1.real<C2.real) or (C1.real==C2.real and C1.imaginary<C2.imaginary)):
            print("Complex Number 1 is Smaller")
        elif((C2.real<C1.real) or (C2.real==C1.real and C2.imaginary<C1.imaginary)):
            print("Complex Number 2 is Smaller")
        else:
            print("Both are equal")


     
# Driver code
if __name__=='__main__':
    
    print("Sakalya Mitra:20MIM10056")
    print("\n")
    # First Complex number
    C1 = Complex(3, 2);
 
    # printing first complex number
    print("Complex number 1 :", C1.real, "+ i" + str(C1.imaginary))
 
    # Second Complex number
    C2 = Complex(9, 5);
 
    # printing second complex number
    print("Complex number 2 :", C2.real, "+ i" + str(C2.imaginary))
     
    # for Storing the sum
    C3 = Complex(0, 0)
 
    # calling addComp() method
    C3 = C3.addComp(C1, C2);
    # printing the ans
    print("Sum of complex number :", C3.real, "+ i"+ str(C3.imaginary))

     # for Storing the subtraction
    C4 = Complex(0, 0)
 
    # calling subComp() method
    C4 = C4.subComp(C1, C2);
    # printing the ans
    print("Subtraction of complex number :", C4.real, "+ i"+ str(C4.imaginary))

     # for Storing the multiplication
    C5 = Complex(0, 0)
 
    # calling mulComp() method
    C5 = C5.mulComp(C1, C2);
    # printing the ans
    print("Multiplication of complex number :", C5.real, "+ i"+ str(C5.imaginary))

    #Checking Equality
    C6 = Complex(0,0)
    C6 = C6.checkEqual(C1,C2)
    if(C6): print("They are equal")
    else: print("They are not equal")

    #Comparing which is greater
    C7 = Complex(0,0)
    C7.checkGreater(C1,C2)