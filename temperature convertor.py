print('Welcome ')

print('Choose the conversion type')
print('1:Celcius to Fahrenheit')
print('2:Celcius to Kelvin')
print('3:Fahrenheit to celcius')
print('4:Fahrenheit to kelvin')
print('5:Kelvin to celcius')
print('6:Kelvin to Fahrenheit')
print('    ')
while True:
    conversion_type=int(input('Enter the number corressponding to your choice: '))

    if conversion_type == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")

    elif conversion_type == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C is equal to {kelvin} K")

    elif conversion_type == 3:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")
   
    elif conversion_type == 4:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(f"{fahrenheit}°F is equal to {kelvin} K")
   
    elif conversion_type == 5:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin} K is equal to {celsius}°C")
   
    elif conversion_type == 6:
        kelvin = float(input("Enter temperature in Kelvin: "))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print(f"{kelvin} K is equal to {fahrenheit}°F")
   
    else:
        print("Invalid choice. Please restart the program and choose a valid conversion type.")

    a=input('Do you want to continue (y/n):')
    if a.lower()=='y': #a.lower() convert any uppercase letter into lowercase
        continue
    else:
        print('Thank you')
        break
