#create dict 
book = {
    "title" : "The Lord of the Rings",
    "author" : "J.R.R Tolkien",
    "pages" : 1867,
    "price" : 650.67 
}
#print dict 
print("\n---Book Details---")
print(f"The book in questions title: {book['title']}")
print(f"Written by: {book['author']}")
print(f"It contains: {book['pages']} pages")
print(f"With a price of: {book['price']:.2f}")
#update price
new_price = float(499.20)
book['price'] = new_price
print()
print("\n---Updated Book Pricing---")
print(f"The book in questions title: {book['title']}")
print(f"Written by: {book['author']}")
print(f"It contains: {book['pages']} pages")
print(f"With a price of: {book['price']:.2f}")