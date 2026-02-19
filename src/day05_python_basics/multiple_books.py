#initialize library storage
library = []
# define book inventory
book1 = {
    "Title" : "Harry Potter",
    "Author" : "J.K. Rowling",
    "Pages" : 320,
    "Price" : 150.00
}

book2 = {
    "Title" : "The Hobbit",
    "Author" : "J.R.R Tolkien",
    "Pages" : 1380,
    "Price" : 250.00
}

book3 = {
    "Title" : "1984",
    "Author" : "George Orwell",
    "Pages" : 328,
    "Price" : 120.00
}
#populate library 
library.append(book1)
library.append(book2)
library.append(book3)
#book search
user_search = input("Enter book title to search: ").lower()
found = False
for book in library:
    if book["Title"].lower() == user_search:
        found = True
        #display book details
        print("\n----Book Found!---")
        print(f"Title {book['Title']}: ")
        print(f"Author {book['Author']}: ")
        print(f"Pages {book['Pages']}: ")
        print(f"Price {book['Price']}: ")
        #update price
        new_price = float(input("Enter new book price: "))
        book["Price"] = new_price
        print(f"Price updated to R{new_price:.2f}")
        break
#handle not found
if not found:
    print("\nBook not found in library!")

#display updated library
print("\n---Updated Library---")
for i, book in enumerate (library, 1):
    print(f"\nBook {i}:")
    print(f"Title: {book['Title']}")
    print(f"Author: {book['Author']}")
    print(f"Pages: {book['Pages']}")
    print(f"Price: {book['Price']:.2f}")




