print()
from statistics import mean
# Entity, Code, Year, Life expectancy

inquire = "yes"

while inquire == "yes":
    inquire = ""
    
    
    i = 0
    with open("../week11/life-expectancy.csv") as life_expectancies:
        i += 1
        
        country_name = ""
        country_largest = 0
        country_lowest = 1000
        country_average = 0
        country = input("Type the country: ")
        country_expectancy = input("Type LARGEST OR LOWEST for life expectancy: ")
        print()
        
        for details in life_expectancies:
            # strip and split
            details_strip = details.strip()
            details_split = details_strip.split(",") # split
            
            # Highest
            if country.title() == details_split[0] and country_expectancy.lower() == "largest":
                
                for i in range(len(details_split)):
                    if float(details_split[3]) > country_largest:
                        country_largest = float(details_split[3])
                        print(f"Largest years of expectancy: {details_split[2]} - {country_largest}")
            
            # Lowest
            elif country.title() == details_split[0] and country_expectancy.lower() == "lowest":
                
                for i in range(len(details_split)):
                    if float(details_split[3]) < country_lowest:
                        country_lowest = float(details_split[3])
                        print(f"Lowest years of expectancy: {details_split[2]} - {country_lowest}")                
            
    
    inquire = input("Do you want to inquire again (yes/no)?")
    print()
    
    
print("Thank you, for inquiring! \n")
        
        
            
            
            
        
        
    
                
                
                

          
