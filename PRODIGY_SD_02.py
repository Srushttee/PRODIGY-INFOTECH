def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    return celsius * 9 / 5 + 32

def convert_temperature(value, unit):
    if unit.lower() == 'c':
        celsius = value
        print(f"{celsius} Celsius is equal to {celsius_to_fahrenheit(celsius):.2f} Fahrenheit")
        print(f"{celsius} Celsius is equal to {celsius_to_kelvin(celsius):.2f} Kelvin")
    elif unit.lower() == 'f':
        fahrenheit = value
        print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit):.2f} Celsius")
        print(f"{fahrenheit} Fahrenheit is equal to {fahrenheit_to_kelvin(fahrenheit):.2f} Kelvin")
    elif unit.lower() == 'k':
        kelvin = value
        print(f"{kelvin} Kelvin is equal to {kelvin_to_celsius(kelvin):.2f} Celsius")
        print(f"{kelvin} Kelvin is equal to {kelvin_to_fahrenheit(kelvin):.2f} Fahrenheit")
    else:
        print("Invalid unit entered. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

def main():
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ")
    convert_temperature(value, unit)

if __name__ == "__main__":
    main()
