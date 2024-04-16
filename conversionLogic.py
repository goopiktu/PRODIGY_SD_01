# Celsius to Fahrenheit
def celsiusToFahrenheit(celsius): 
    return (celsius * 1.8) + 32

# Celsius to Kelvin
def celsiusToKelvin(celsius):
    return celsius + 273.15

# Kelvin to Celsius
def kelvinToCelsius(kelvin):
    return kelvin - 273.15

# Kelvin To Fahrenheit
def kelvinToFahrenheit(kelvin):
    return kelvinToCelsius(kelvin) * 1.8 + 32

# Fahrenheit To Celsius
def FahrenheitToCelsius(Fahrenheit):
    return (Fahrenheit - 32) * 0.5555555556

# Fahrenheit To Kelvin
def FahrenheitToKelvin(Fahrenheit):
    return FahrenheitToCelsius(Fahrenheit) + 273.15



def main(firstArg, secondArg, firstEntry):

    print(firstArg + " " + secondArg + " " + str(firstEntry))

    option = firstArg + " to " + secondArg
    match option:
        case "Celsius to Fahrenheit":
            return celsiusToFahrenheit(firstEntry)
        
        case "Celsius to Kelvin":
            return celsiusToKelvin(firstEntry)
        
        case "Kelvin to Celsius":
            return kelvinToCelsius(firstEntry)
        
        case "Kelvin to Fahrenheit":
            return kelvinToFahrenheit(firstEntry)
        
        case "Fahrenheit to Celsius":
            return FahrenheitToCelsius(firstEntry)
        
        case "Fahrenheit to Kelvin":
            return FahrenheitToKelvin(firstEntry)
        