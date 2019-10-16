from math import sqrt
print("Enter 'x' to go back. ")
formula = input('Which side (a,b c) you want to calculate? side> ')
if formula == 'x':
    import MHOME
if formula == 'c' :
    side_a = int(input("Enter the length of side a: "))
    side_b = int(input("Enter the length of side b: "))

    side_c = sqrt(side_a * side_a + side_b * side_b)
    print("The length of side c is: " )
    print(side_c)

elif formula == 'a':
    side_b = int(input("Enter the length of side b: "))
    side_c = int(input("Enter the length of side c: "))
     
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    print("The length of side a is" )
    print(side_a)

elif formula == 'b':
    side_a = int(input("Enter the length of side a: "))
    side_c = int(input("Enter the length of side c: "))

    side_b = sqrt(side_c * side_c - side_a * side_a)
    print("The length of side b is" )
    print(side_b)

else:
    print("Please select a side between a, b, c")





