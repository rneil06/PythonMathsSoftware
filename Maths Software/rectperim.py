print("Enter 'x' to go back. ")
leng = input("Enter length of rectangle: ")
if leng == 'x':
    import MHOME
else:
    brea = input("Enter breadth of rectangle: ")
    length = int(leng)
    breadth = int(brea)
    perimeter = (2*length) + (2*breadth)
    print("\nPerimeter of Rectangle =", perimeter)