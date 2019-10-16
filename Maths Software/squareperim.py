print("Enter 'x' to go back. ")
side = input("Enter side length of square: ")
if side == 'x':
   import MHOME
else:
    slength = int(side)
    perimeter = 4*slength
    print("\nPerimeter of Square = ", perimeter)