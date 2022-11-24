print()
# Wind Chill Calculations 

# Wind Chill
# Fahrenheit to Celcius = C = 5/9 (F - 32)
# Celcius to Fahrenheit = F = C (9 / 5) + 32

# Wind Chill
def wind_chill(temp, wind_speed=0):
    return (35.74 + 0.6215 * temp) - (35.75 * wind_speed ** 0.16) + (0.4275 * wind_speed ** 0.16)

      
# Fahrenheit
def fahrenheit(temp):
    return temp * (9 / 5) + 32

# Celcius
def celcius(temp):
    return 5/ 9 * (temp - 32)


def temp_compute(temp_type, value1):
    temperature = -1
    
    if temp_type == "F":
        temperature = fahrenheit(value1)
    elif temp_type == "C":
        temperature = celcius(value1)
        
    return temperature


# Main program
temp_type = ""

while temp_type != "":
    temp_num = float(input("What is the temperature? "))
    temp_type = input("Fahrenheit or Celcius (F/C)? ")
    
    temp_type.upper()
    
    if temp_type == "F":
        temperature = temp_compute(temp_type, temp_num)
        print(temperature)
    elif temp_type == "C":
        temperature = temp_compute(temp_type, temp_num)
        print(temperature)
        
    

    