print()

with open("scriptures12.txt") as scriptures:
    for scripture in scriptures:
        scripture_strip = scripture.strip() # Remove extra spaces
        scripture_split = scripture_strip.split(":") # Separate items
        
        # Access index
        scriptures_name = scripture_split[2] 
        books = scripture_split[0]
        books_chapters = scripture_split[1]
        
        
        
        
        
        
        
        
        