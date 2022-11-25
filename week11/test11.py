print()

with open("life-expectancy.csv") as life_expectancies:
   
    i = 0
    # Lowest
    lowest_expectancy = 1000
    lowest_country = ""
    lowest_year = 0
    
    average_life_exp = 0
    
    # Highest
    highest_expectancy = 0
    highest_country = ""
    highest_year = 0
    
    
    highest_expectancy = 0
    for life in life_expectancies:
        i += 1
        # print(f"{i} - {life}")
        life_strip = life.strip()
        life_split = life_strip.split(",")
        country = life_split[0] # Country
        code = life_split[1] # Code
        year = life_split[2] # Year
        life_exp = life_split[3] # Life Expectancy STRING
        
    
        if i > 1:
            life_exp = float(life_exp)
          
            if life_exp < lowest_expectancy:
                lowest_expectancy = life_exp
                lowest_country = country
                lowest_year = year
                
                average_life_exp = average_life_exp + life_exp
                
            if life_exp > highest_expectancy:
                highest_expectancy = life_exp
                highest_country = country
                highest_year = year

# print(f"The average of all is {average_life_exp}")
print(f"{lowest_country} - {lowest_year} - {lowest_expectancy}")
print(f"{highest_country} - {highest_year} - {highest_expectancy}")
print()

        
        