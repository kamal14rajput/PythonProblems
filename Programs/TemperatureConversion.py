def tempConversion(celcius, fahrenheit):
    #Converting Celsius to Fahrenheit
    fah = (celcius * 9/5) + 32
    print("After Converting to fahrenheit:", fah)

    # Converting Fahrenheit to Celsius
    cel = (fahrenheit - 32) * 5/9
    print("After Converting to celcius:", cel)

#user inputs
celcius = int(input("Enter the temperature in celcius:"))
fahrenheit = int(input("Enter the temperature in fahrenheit:"))

tempConversion(celcius, fahrenheit)