print()
i = 0
num_years = 0
import statistics

with open("../week11/life-expectancy.csv") as life_expectancies:
    year_of_interest = int(input("Enter the year of interest: "))
    
    max_life_all = ""
    min_life_all = ""
    max_life_all_exp = 0
    min_life_all_exp = 1000
    
    ave_life_exp = 0
    
    max_life_country = ""
    min_life_country = ""
    max_life_exp = 0
    min_life_exp = 1000
    
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
                
                if life_exp > max_life_all_exp:
                    max_life_all_exp = life_exp
                    max_life_all = country
                    
                if life_exp < min_life_all_exp:
                    min_life_all_exp = life_exp
                    min_life_all = country
                    
                if year_of_interest == year:
                    ave_life_exp = ave_life_exp + life_exp
                    num_years += 1
                        
                     
                    if life_exp > max_life_exp:
                        max_life_exp = life_exp
                        max_life_country = country  
                    
                    if life_exp < min_life_exp:
                        min_life_exp = life_exp
                        min_life_country = country
                 

print(f"The overall max life expectancy is: {max_life_all_exp} from {max_life_all} in {year}")
print(f"The overall min life expectancy is: {min_life_all_exp} from {min_life_all} in {year} \n")


print(f"For the year {year_of_interest}:")
print(f"The average life expectancy across all the countries was {(ave_life_exp / num_years):.2f}")
print(f"The max life expectancy was in {max_life_country} with {max_life_exp:.2f}")
print(f"The min life expectancy was in {min_life_country} with {min_life_exp}")
print()



