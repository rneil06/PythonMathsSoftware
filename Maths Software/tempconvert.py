# Converting Fahrenheit to Celsius
print("Enter 'x' to go back. ")
fah = input("Enter Temperature in Fahrenheit: ")
if fah == 'x':
    import MHOME
else:
    fahrenheit = float(fah)
    celsius = (fahrenheit-32)/1.8
    print("Temperature in Celsius = ", celsius)