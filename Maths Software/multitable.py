print("Enter 'x' to go back. ")
num = input("Enter a number: ")
if num == 'x':
    import MHOME
else:
    number = int(num)
    for i in range(1,11):
        print(number, "*", i, "=", number*i)
