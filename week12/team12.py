print()

# Largest number
scripture_largest_num = 0
scripture_largest_num_book = ""

with open("scriptures12.txt") as scriptures:
    for scripture in scriptures:
        scripture_strip = scripture.strip() # Remove extra spaces
        scripture_split = scripture_strip.split(":") # Separate items
        # print(scripture_split)
     
        # Display format
        # print(f"Scripture: {scripture_split[2]}, Book: {scripture_split[0]}, Chapters: {scripture_split[1]}")
        
        # Largest number
        if int(scripture_split[1]) > scripture_largest_num:
            scripture_largest_num = int(scripture_split[1])
            scripture_largest_num_book = scripture_split[0]
            
            if scripture_largest_num == 150:
                print(f"The {scripture_largest_num_book} has the largest scripture verses it has {scripture_largest_num}.")
    
    
        
        
        
        
        
        
        