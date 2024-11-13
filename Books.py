# Book 1
book_1 = {
    "id": "1",
    "title": "A Tale of Two Cities",
    "author": "Charles Dickens",
    "release": "1859",
    "sold": "200+ million",
}

# Book 2
book_2 = {
    "id": "2",
    "title": "Le Petit Prince",
    "author": "Antoine de Saint0-Exupery",
    "release": "French",
    "sold": "200 million",
}

# Book 3
book_3 = {
    "id": "3",
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "release": "1988",
    "sold": "150 million",
}

# Book 4
book_4 = {
    "id": "4",
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "release": "1997",
    "sold": "120 million",
}

# Book 5
book_5 = {
    "id": "5",
    "title": "And Then There Were None",
    "author": "Agatha Christie",
    "release": "1939",
    "sold": "100 million",
}

# Book 6
book_6 = {
    "id": "6",
    "title": "Dream of the Red Chamber",
    "author": "Cao Xueqin",
    "release": "1791",
    "sold": "100 million",
}

# Book 7
book_7 = {
    "id": "7",
    "title": "The Hobbit",
    "author": "J. R. R. Tolkein",
    "release": "1937",
    "sold": "100 million",
}

# Book 8
book_8 = {
    "id": "8",
    "title": "Alice's Adventures in Wonderland",
    "author": "Lewis Carroll",
    "release": "1865",
    "sold": "100 million",
}

# Book 9
book_9 = {
    "id": "9",
    "title": "The Da Vinci Code",
    "author": "Dan Brown",
    "release": "2003",
    "sold": "80 million",
}

books = [book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8, book_9]

for book in books:
    print(f"ID: {book.get('id')}, Title: {book.get('title')}, Author: {book.get('author')}, Release Date: {book.get('release')}, Copies Sold: {book.get('sold')}")