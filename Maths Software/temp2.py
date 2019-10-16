# Celsius to Fahrenheit converter
print("Enter 'x' to go back. ")
cel = input("Enter Temperature in Celsius: ")
if cel == 'x':
    import MHOME
else:
    celsius = float(cel)
    Fahrenheit = (1.8*celsius) + 32
    print("Temperature in Fahrenheit = ", Fahrenheit)