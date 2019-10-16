print("Enter 'x' to go back. ")
num = input("Enter a number: ")
if num == 'x':
    import MHOME
else:
    number = float(num)
    number_sqrt = number ** 0.5
    print("Square Root of %0.2f is %0.2f" %(number, number_sqrt))