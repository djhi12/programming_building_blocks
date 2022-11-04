print()
# Entity, Code, Year, Life expectancy
# Variables
# year = None


with open("life-expectancy.csv") as life_expectancies:
    # Highest
    highest = 86
    highest_country = ""
    highest_year = 0
    
    # Lowest
    lowest = 1000
    lowest_country = ""
    lowest_year = 0
    
    # Average
    # from statistics import mean 
    average = 43
    average_country = ""
    average_year = 0

    
    i = 0
    for life in life_expectancies:
        i += 1
        life_details = life.strip()
        life_detail_clean = life_details.split(",")

        if i > 1:
            # highest country/year
            if highest < float(life_detail_clean[3]):
                highest = float(life_detail_clean[3])
                highest_year = life_detail_clean[2]
                highest_country = life_detail_clean[0]

                print(f"Highest {highest} - {highest_year} - {highest_country}")
         
            # Lowest country/year
            elif lowest > float(life_detail_clean[3]):
                lowest = float(life_detail_clean[3])
                lowest_year = life_detail_clean[2]
                lowest_country = life_detail_clean[0]

                print(f"Lowest {lowest} - {lowest_year} - {lowest_country}")
                
            #Average country/year
            elif average == float(life_detail_clean[3]):
                average =float(life_detail_clean[3])
                average_year = life_detail_clean[2]
                average_country = life_detail_clean[0]
                
                print(f"Average {average} - {average_year} - {average_country}")
                
                
                

          
