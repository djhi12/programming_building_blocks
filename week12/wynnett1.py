
i = 0

# Specific variables for the inputted year of interest
max_life = 0
max_place = ""
max_year = 0

min_life = 1000
min_place = ""
min_year = 0

ave_life_expectancy = 0
num_yrs = 0
chosen_country = ""

print()
country_name = input("Enter what country you're interested in: ")

with open("life-expectancy.csv") as life_exp: # To open other/new file (could be txt, cvs, etc)
    for orig_data in life_exp:
        i += 1 #to count how many lines are there in the file
        updated_data = orig_data.strip() # To clean up the file
        data = updated_data.split(",") # To split using comma

        country = data[0]
        code = data[1]
        year = data[2]
        life_expectancy = data[3]

        if country_name == country:
            life_expectancy = float(life_expectancy) # Need to convert string to float
            ave_life_expectancy = ave_life_expectancy + life_expectancy
            num_yrs += 1


            if life_expectancy > max_life:
                max_life = life_expectancy
                max_place = country
                max_year = year

            if life_expectancy < min_life:
                min_life = life_expectancy
                min_place = country
                min_year = year

# Should be outside the for loop
print(f"The overall max life expectancy is: {max_life:.2f} in {max_year}") 
print(f"The overall min life expectancy is: {min_life:.2f} in {min_year}") 
print(f"The average life expectancy across all countries was {(ave_life_expectancy / num_yrs):.2f}")

print()