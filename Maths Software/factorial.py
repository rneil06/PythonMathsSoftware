print("Enter 'x' to go back")
num = input("Enter a number to find its factorial: ")
if num == 'x':
    import MHOME
else:
    number = int(num)
    if number == 0:
        print("\nFactorial of 0 is 1")
    elif number < 0:
        print("\nFactorial of negative numbers does not exist! ")
    else:
        fact = 1
        for i in range(1, number+1):
            fact = fact*i
        print("Factorial of" ,number ,"is", fact)
