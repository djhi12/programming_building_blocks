print()

with open("scriptures12.txt") as scriptures:
    for scripture in scriptures:
        scripture_strip = scripture.strip() # Remove extra spaces
        scripture_split = scripture_strip.split(":") # Separate items
        # print(scripture_split)
     
        # Book of Mormon
        for i in range(len(scripture_split)):
            books_of_mormon = scripture_split[i]
            book_of_mormon = scripture_split[i]
            book_of_mormon_chap = int(scripture_split[1])
            
            if books_of_mormon == "Book of Mormon":
                 print(books_of_mormon)
                
            
        
        
        
        
        
        
        
        