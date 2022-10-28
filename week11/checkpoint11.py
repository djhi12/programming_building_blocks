print()

with open("bom.txt") as scriptures:
    for book in scriptures:
        book_clean = book.strip()
        print(book_clean)
print()
