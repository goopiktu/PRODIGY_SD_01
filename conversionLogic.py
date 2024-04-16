
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
    

def main(firstArg, firstEntry):

    match firstArg:
        case "Celsius":
            fahrenheit = celsiusToFahrenheit(firstEntry)
            kelvin = celsiusToKelvin(firstEntry)
            fahrenheit = round(fahrenheit, 3)
            kelvin = round(kelvin, 3)
            return (f"{fahrenheit}℉"),(f"{kelvin}K")   
        
        case "Kelvin":
            celsius = kelvinToCelsius(firstEntry)
            fahrenheit = kelvinToFahrenheit(firstEntry)
            celsius = round(celsius, 3)
            fahrenheit = round(fahrenheit, 3)
            return (f"{fahrenheit}℉"),(f"{celsius}℃") 
        
        case "Fahrenheit":
            celsius = FahrenheitToCelsius(firstEntry)
            kelvin = FahrenheitToKelvin(firstEntry)
            celsius = round(celsius, 3)
            kelvin = round(kelvin, 3)
            return (f"{kelvin}K"),(f"{celsius}℃")   