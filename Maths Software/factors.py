print("Enter 'x' to go back. ")
num = input("Enter a number: ")
if num == 'x':
    import MHOME
else:
    count = 0
    number = int(num)
    for i in range(2, number-1):
        if number%i == 0:
            print(i)
            i +=1
            count += 1
    if count == 0:
        print(number, "is a prime number. ")


