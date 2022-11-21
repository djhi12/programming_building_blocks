print()
# from statistics import mean
# # Entity, Code, Year, Life expectancy

# inquire = "yes"

# while inquire == "yes":
#     inquire = ""
    
    
#     i = 0
#     with open("../week11/life-expectancy.csv") as life_expectancies:
#         i += 1
        
#         country_name = ""
#         country_largest = 0
#         country_lowest = 1000
#         country_average = 0
#         country = input("Type the country: ")
#         country_expectancy = input("Type LARGEST OR LOWEST for life expectancy: ")
#         print()
        
#         for details in life_expectancies:
#             # strip and split
#             details_strip = details.strip()
#             details_split = details_strip.split(",") # split              
            
    
inquire = "yes"

while inquire == "yes":
    inquire = ""
    with open("../week11/life-expectancy.csv") as life_expectancies:
        country_name = ""
        country_largest = 0
        country_lowest = 1000
        country_average = 0
        
        
        print()
        i = 0
        max_life_expectancy = 0
        min_life_expectancy = 1000
        average_life_ecpectancy = 0
        year_of_interest = int(input("Enter the year of interest: "))
        country = input("Type the country: ")
        country_expectancy = input("Type LARGEST OR LOWEST for life expectancy: ")
        
        for details in life_expectancies:
            i += 1
            # strip and split
            details_strip = details.strip()
            details_split = details_strip.split(",") # split
            # details_split_float = float(details_split[3])
            
            if i > 1:
                details_split_float = float(details_split[3])
                details_split_year = int(details_split[2])
                
                if details_split_year == year_of_interest:
                    
                    # print(max(details_split_float))
                    if details_split_float > max_life_expectancy:
                        max_life_expectancy = details_split_float
                
                        
                    elif details_split_float < min_life_expectancy:
                        min_life_expectancy = details_split_float
                        
            # Highest
            if country.title() == details_split[0] and country_expectancy.lower() == "largest":
                
                for i in range(len(details_split)):
                    if float(details_split[3]) > country_largest:
                        country_largest = float(details_split[3])
                        
            
            # Lowest
            elif country.title() == details_split[0] and country_expectancy.lower() == "lowest":
                
                for i in range(len(details_split)):
                    if float(details_split[3]) < country_lowest:
                        country_lowest = float(details_split[3])
                        
                                            
        
        print(f"The overall max life expectancy is: {max_life_expectancy} from {details_split[0]} in {details_split_year}")        
        
        print(f"The overall min life expectancy is: {min_life_expectancy} from {details_split[0]} in {details_split_year} \n")

        print(f"For the year {year_of_interest}:")
        print(f"The average life expectancy across all countries was {average_life_ecpectancy}")
        print(f"The max life expectancy was in {details_split[0]} with {max_life_expectancy}")
        print(f"The min life expectancy was in {details_split[0]} with {min_life_expectancy} \n")
        print(f"Largest years of expectancy: {details_split[2]} - {country_largest}")
        print(f"Lowest years of expectancy: {details_split[2]} - {country_lowest}")
    
    inquire = input("Do you want to inquire again (yes/no)?")
    print()
    
    
print("Thank you, for inquiring! \n")
                        
                        
            
                    
            
            
           
            
       
             
             
    



        
        
            
            
            
        
        
    
                
                
                

          
