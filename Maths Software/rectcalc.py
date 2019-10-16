print("Enter 'x' to go back. ")
leng = input("Enter length of Rectangle: ")
if leng == 'x':
    import MHOME
else:
    brea = input("Enter breadth of Rectangle: ")
    length = int(leng)
    breadth = int(brea)
    area = length*breadth
    print("\nArea of Rectangle =", area)