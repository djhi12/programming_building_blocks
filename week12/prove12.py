print()
# Entity, Code, Year, Life expectancy

inquire = "yes"

while inquire == "yes":
    inquire = ""
    
    
    i = 0
    with open("../week11/life-expectancy.csv") as life_expectancies:
        i += 1
        country_name = ""
        country_largest = 0
        country = input("Type the country: ")
        
        
        for details in life_expectancies:
            # strip and split
            details_strip = details.strip()
            details_split = details_strip.split(",")
            
        
            if country.title() == details_split[0]:
                
                # for i in range(len(details_split)):
                #     print(f"Country: {details_split[0]} - Code: {details_split[1]} - Year: {details_split[2]} - Life Expectancy: {float(details_split[3])}")
                    
                if float(details_split[3]) > country_largest:
                    country_largest = float(details_split[3])
                    country_name = details_split[0]
                    
                    print(f"{country_name} - {country_largest}")
                    
               
        
        # 
    
    
    
    
    
    
    inquire = input("Do you want to inquire again (yes/no)?")
    
    
print("Thank you, for inquiring!")
        
        
            
            
            
        
        
    
                
                
                

          
