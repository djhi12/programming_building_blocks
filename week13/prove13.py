print()
# Wind Chill Calculations 

# Wind Chill (ºF) = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T *(V0.16)
# Where,T= Air Temperature (ºF) V= Wind Speed (mph)

# Celcius = C = 5/9 (F - 32)
# Fahrenheit = F = C (9 / 5) + 32

# Wind Chill
def wind_chill(air_temp, wind_speed):
    # return (35.74 + 0.6215 * temp) - (35.75 * wind_speed ** 0.16) + (0.4275 * wind_speed ** 0.16)
    return 35.74 + (0.6215 * air_temp) - (35.75 * wind_speed**0.16) + (0.4275 * air_temp * wind_speed**0.16)

      
# Fahrenheit
def fahrenheit(temp):
    return temp
    

# Celcius
def celcius(temp):
    return temp * (9 / 5) + 32


# Compute temp
def temp_compute(temp_type, value1):
    temperature = -1
    
    if temp_type.upper() == "F":
        temperature = fahrenheit(value1)
    elif temp_type.upper() == "C":
        temperature = celcius(value1)
        
    return temperature


# Main program
temp_type = ""

while temp_type != "QUIT":
    temp_num = float(input("What is the temperature? "))
    temp_type = input("Fahrenheit or Celcius (F/C)? ")
    
    
    temp_type = temp_type.upper()
    
    if temp_type == "F":
        temperature = temp_compute(temp_type, temp_num)
        wind_speed = 0
        air_temp = 0
        
        for i in range(12):
            wind_speed = wind_speed + 5
            # air_temp = air_temp + 5
            
            # print(temperature)
            print(f"At temperature {temperature}F, and the wind speed {wind_speed} mph, the windchill is: {wind_chill(temp_num, wind_speed)}F")
            
    elif temp_type == "C":
        temperature = temp_compute(temp_type, temp_num)
        wind_speed = 0
        air_temp = 14
       
        
        for i in range(12):
            wind_speed = wind_speed + 5
            air_temp = air_temp - 0.001
       
            
            # print(temperature)
            print(f"At temperature {temperature}F, and the wind speed {wind_speed} mph, the windchill is: {wind_chill(air_temp, wind_speed):.2f}F")
        
        

    
        
    

    