print("Enter 'x' to go back. ")
rad = input("Enter radius of circle: ")
if rad =='x':
    import MHOME
else:
    radius = float(rad)
    area = 3.14 * radius * radius
    print("\nArea of Circle = %0.2f" %area)
