print()

with open("life-expectancy.csv") as life_expectancies:
    year_of_interest = int(input("Enter the year of interest: "))
    i = 0
    # Lowest
    lowest_expectancy = 1000
    lowest_country = ""
    lowest_year = 0
    
    # Average
    average_life_exp = 0
    
    # Highest
    highest_expectancy = 0
    highest_country = ""
    highest_year = 0
    
    
    highest_expectancy = 0
    
    # Year of interest
    max_life = 0
    max_place = ""
    max_year = 0
    
    min_life = 1000
    min_place = ""
    min_year = 0
    
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
                
            if life_exp > highest_expectancy:
                highest_expectancy = life_exp
                highest_country = country
                highest_year = year
                
            if year_of_interest == year:
                # 
                if life_exp < max_life:
                    max_life = life_exp
                    max_year = year
                    max_place = country
                    
                if life_exp < min_life:
                    min_life = life_exp
                
                
                


# print(f"The overall max life expectancy is: {highest_expectancy} from {highest_country} in {highest_year} ")
# print(f"The overall min life expectancy is: {lowest_expectancy} from {lowest_country} in {lowest_year} ")
        
        