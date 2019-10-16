print("Enter 'x' to go back. ")
side = input("Enter side length of Square: ")
if side == 'x':
    import MHOME
else:
    side_length = int(side)
    area_square = side_length*side_length
    print("\nArea of Square =",area_square)
