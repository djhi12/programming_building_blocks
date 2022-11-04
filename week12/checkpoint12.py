print()

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"]

age_youngest = 5
name_youngest = ""

for name in people:
    name_split = name.split()
    name_age = int(name_split[1]) # Age
    name_rank = name_split[0] # Name
    
    if name_age < age_youngest:
        age_youngest = name_age
        name_youngest = name_rank
        
        # print(age_youngest)
        # print(name_youngest)
        
        print(f"The youngest among the names is {name_youngest} - {age_youngest}")
    
        
       
    
    
    
    
    
   
