print("Enter 'x' to go back. ")
side1 = input("Enter length of first side: ")
if side1 == 'x':
    import MHOME
else:
    side2 = input("Enter length of second side: ")
    side3 = input("Enter length of third side: ")
    a = float(side1)
    b = float(side2)
    c = float(side3)
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("\nArea of Triangle = %0.2f" %area)