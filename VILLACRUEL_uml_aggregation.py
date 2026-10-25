# Aggregation
class Book:
    pass

class Library:
    def __init__(self, book: Book):
        self.book = book

# (Test)
novel = Book()
shelf = Library(novel)
print(shelf.book is novel)
