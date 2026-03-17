from app import Library
class book:
    def __init__(self,book_id,book_name):
        self.book_id = book_id 
        self.book_name = book_name 
        self.available = True
    
    def viewBook(self):
        rec = Library.books
        for i in rec:
            print(i.book_id,i.book_name,i.available)
    
    def viewBook_id(self,book_id):
        for b in Library.books:
            if b.book_id == book_id:
                print(b.book_id, b.book_name, b.available)

    
