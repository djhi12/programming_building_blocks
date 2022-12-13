i = 0

# Lowest
lowest_exp = 1000
lowest_country = ""
lowest_year = 0

# Highest
highest_exp = 0
highest_country = ""
highest_year = 0

# Specific variables for the inputted year of interest
max_life = 0
max_place = ""
max_year = 0

min_life = 1000
min_place = ""
min_year = 0

num_yrs = 0
ave_life_expectancy = 0

print()
input_year = input("Enter the year of interest: ")

with open("../week11/life-expectancy.csv") as life_exp: # To open other/new file (could be txt, cvs, etc)
    for orig_data in life_exp:
        i += 1 #to count how many lines are there in the file
        updated_data = orig_data.strip() # To clean up the file
        data = updated_data.split(",") # To split using comma

        country = data[0]
        code = data[1]
        year = data[2]
        life_expectancy = data[3]

        if i > 1: # skip the first line/title of the csv file
            life_expectancy = float(life_expectancy) # To convert string to float, should be inside the if statement and not outside

            if life_expectancy < lowest_exp:
                lowest_exp = life_expectancy
                lowest_country = country
                lowest_year = year
            
            if life_expectancy > highest_exp:
                highest_exp = life_expectancy
                highest_country = country
                highest_year = year

            if input_year == year:
                ave_life_expectancy = ave_life_expectancy + life_expectancy
                num_yrs += 1

                if life_expectancy > max_life:
                    max_life = life_expectancy
                    max_place = country

                if life_expectancy < min_life:
                    min_life = life_expectancy
                    min_place = country

print(f"The overall max life expectancy is: {highest_exp} from {highest_country} in {highest_year}") # Should be outside the for loop
print(f"The overall min life expectancy is: {lowest_exp} from {lowest_country} in {lowest_year}") # Should be outside the for loop

print()        

print(f"For the year {input_year}:")

print(f"The average life expectancy across all countries was {(ave_life_expectancy / num_yrs):.2f}")
print(f"The max life expectancy was {max_place} with {max_life}") 
print(f"The min life expectancy was {min_place} with {min_life}") 

print() 