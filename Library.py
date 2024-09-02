

class Book:
    def __init__(self, bookId, title, author, releaseDate, pages, description, publisher):
        self.bookId = bookId
        self.title = title
        self.author = author
        self.releaseDate = releaseDate
        self.pages = pages
        self.description = description
        self.publisher = publisher

BookList = []
       



print("Welcome to the library program")
print("-"*25)

searchOrAdd = input("Do you want to Search or Add a book to the database (Add or Search): ")

if searchOrAdd.lower() == "add":  
    

elif searchOrAdd.lower() == "search":


else:
    print("No valid option was selected.")
    #test