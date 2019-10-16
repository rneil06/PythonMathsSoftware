#Home page for software

print('Welcome to the most advanced maths software')
print('1. Simple Calculator')
print('2. Kilometres to Miles Converter')
print('3. Fahrenheit to Celsius Converter')
print('4. Celsius to Fahrenheit Converter')
print('5. Average Percentage Calculator')
print('6. Area Calculator')
print('7. Perimeter Calculator')
print('8. Square Root Calculator')
print('9. Multiplication Tables')
print('10. Prime Numbers Tables')
print('11. Factors Calculator')
print('12. Quadratic Equations Solver')
print('13. Factorials Finder')
print('14. Pythagorean Theorem Solver')
print('15. Speed, Distance, Time Calculator')

print("Enter 'x' to go back. ")
choice = int(input('Enter your choice: '))

if choice == 'x':
    import HOME
if choice == 1:
    import simplecalculator
if choice == 2:
      import kmmi
if choice == 3:
    import tempconvert
if choice == 4:
    import temp2
if choice == 5:
    import percentcalc
if choice == 6:
    import areacalc
if choice == 7:
    import perimcalc
if choice == 8:
    import rootcalc
if choice == 9:
    import multitable
if choice == 10:
    import primetable
if choice == 11:
    import factors
if choice == 12:
    import quadcalc
if choice == 13:
    import factorial
if choice == 14:
    import pythags
if choice == 15:
    import sdtcalc

#Add more if choices (AM DOING SO)
#Possibly add personals like name !!!!!!!!INVESTIGATE!!!!!!!!!!!!
#Add advanced calculator
#Add time converter in analogue to digital and the world clocks

