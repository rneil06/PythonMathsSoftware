print("Enter 'x' to go back. ")
len1 = input("Enter lenght of first side: ")
if len1 == 'x':
    import MHOME
else:
    len2 = input("Enter length of second side: ")
    len3 = input("Enter length of thir side: ")
    length1 = int(len1)
    length2 = int(len2)
    length3 = int(len3)
    perimeter = length1 + length2 + length3
    print("\nPerimeter of Triangle =", perimeter)