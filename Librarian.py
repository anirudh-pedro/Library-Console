from app import Library
from book import book

class Librarian:
    def __init__(self,Librarian_name, Librarian_id,Librarian_email):
        self.Librarian_name = Librarian_name
        self.Librarian_id = Librarian_id 
        self.Librarian_email = Librarian_email
    
    def addBooks(self,book_name,book_id):
        Book = book(book_id,book_name)
        Library.books.append(Book)
    
    def deleteBooks(self,book_id,book_name):
        for b in Library.books:
            if b.book_id == book_id:
                Library.books.remove(b)
                print("Book deleted successfully")
                return
        print("Book not found")
    