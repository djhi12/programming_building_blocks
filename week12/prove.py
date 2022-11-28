print()
i = 0

import statistics

with open("../week11/life-expectancy.csv") as life_expectancies:
    country_name = input("Type the country: ")
    
    max_life_exp = 0
    min_life_exp = 1000
    average_life_exp = 0
    
    max_life_year = 0
    min_life_year = 1000
    average_life_year = 0
    
    num_years = 0
    
    for details in life_expectancies:
            i += 1
            
            # strip and split
            details_strip = details.strip()
            details_split = details_strip.split(",") # split
            
            if i > 1:
                year = int(details_split[2])
                life_exp = float(details_split[3])
                country = details_split[0]
                code = details_split[1]
                
                if country.lower() == country_name.lower():
                    average_life_exp = average_life_exp + life_exp
                    num_years += 1
                    average_life_year = year
                    
                    if life_exp > max_life_exp:
                        max_life_exp = life_exp
                        max_life_year = year
                
                        if life_exp < min_life_exp:
                            min_life_exp = life_exp
                            min_life_year = year
                            
    
print()                
print(f"Name of the country: {country_name.capitalize()}")                    
print(f"The maximum life expectancy of the country is {max_life_exp} in the year {max_life_year}")
print(f"The minimum life expectancy of the counntry is {min_life_exp} in the year {min_life_year}")
print(f"The average of life expectancy of the country is {(average_life_exp / num_years):.2f} in the year {average_life_year}")
                 




