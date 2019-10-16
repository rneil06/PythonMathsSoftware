print("Enter 'x' to go back. ")
rad = input("Enter radius of circle: ")
if rad == 'x':
    import MHOME
else:
    radius = float(rad)
    circumference = 2*3.14*radius
    print("\nCircumference of Circle = ", circumference)