class Complex ():
    def initComplex(self):
        self.realPart = int(input("Enter the Real Part: "))
        self.imgPart = int(input("Enter the Imaginary Part: ")) 
    def display(self):
        print(self.realPart,"+",self.imgPart,"i", sep="")
    def sum(self, c1, c2):
        self.realPart = c1.realPart + c2.realPart
        self.imgPart = c1.imgPart + c2.imgPart
    def difference(self, c1, c2):
        self.realPart = c1.realPart - c2.realPart
        self.imgPart = c1.imgPart - c2.imgPart
    def product(self, c1, c2):
        self.realPart = c1.realPart * c2.realPart
        self.imgPart = c1.imgPart * c2.imgPart
c1 = Complex()
c2 = Complex()
c3 = Complex()
c4=Complex()
c5=Complex()
print("Enter first complex number")
c1.initComplex()
print("First Complex Number: ", end="")
c1.display()
print("Enter second complex number")
c2.initComplex()
print("Second Complex Number: ", end="")
c2.display()
print("Sum of two complex numbers is ", end="")
c3.sum(c1,c2)
c3.display()
print("Difference of two complex numbers is ", end="")
c4.difference(c1,c2)
c4.display()
print("Product of two complex numbers is ", end="")
c5.product(c1,c2)
c5.display()



''' OUTPUT
Enter first complex number
Enter the Real Part: 5
Enter the Imaginary Part: 3
First Complex Number: 5+3i
Enter second complex number
Enter the Real Part: 3
Enter the Imaginary Part: 1
Second Complex Number: 3+1i
Sum of two complex numbers is 8+4i
Difference of two complex numbers is 2+2i
Product of two complex numbers is 15+3i '''