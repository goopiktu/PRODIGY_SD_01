# Celsius to Farenheit
def celsiusToFarenheit(celsius): 
    return (celsius * 1.8) + 32

# Celsius to Kelvin
def celsiusToKelvin(celsius):
    return celsius + 273.15

# Kelvin to Celsius
def kelvinToCelsius(kelvin):
    return kelvin - 273.15

# Kelvin To Farenheit
def kelvinToFarenheit(kelvin):
    return kelvinToCelsius(kelvin) * 1.8 + 32

# Farenheit To Celsius
def farenheitToCelsius(farenheit):
    return (farenheit - 32) * 0.5555555556

# Farenheit To Kelvin
def farenheitToKelvin(farenheit):
    return farenheitToCelsius(farenheit) + 273.15



def main(firstArg, secondArg, firstEntry):

    print(firstArg + " " + secondArg + " " + str(firstEntry))

    option = firstArg + " to " + secondArg
    match option:
        case "Celsius to Farenheit":
            return celsiusToFarenheit(firstEntry)
        
        case "Celsius to Kelvin":
            return celsiusToKelvin(firstEntry)
        
        case "Kelvin to Celsius":
            return kelvinToCelsius(firstEntry)
        
        case "Kelvin to Farenheit":
            return kelvinToFarenheit(firstEntry)
        
        case "Farenheit to Celsius":
            return farenheitToCelsius(firstEntry)
        
        case "Farenheit to Kelvin":
            return farenheitToKelvin(firstEntry)
        