import cmath
print("Enter 'x' to go back. ")
num1 = input("Enter value of a: ")
if num1 == 'x':
    import MHOME
else:
    num2 = input("Enter value of b: ")
    num3 = input("Enter value of c: ")
    number1 = float(num1)
    number2 = float(num2)
    number3 = float(num3)
    d = (number2**2) - (4*number1*number3)
    r1 = (-number2-cmath.sqrt(d))/(2*number1)
    r2 = (-number2+cmath.sqrt(d))/(2*number1)
    print("The solutions = {0} and {1}" .format(r1,r2))
