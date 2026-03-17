from app import Library


class Student:
    def __init__(self,name,user_id,email):
        self.name = name 
        self.user_id = user_id
        self.email = email
        Library.users.append(self)
    

    def borrow(self,book_id,start_date,end_date):
        Library.records.append((self.user_id,book_id, start_date, end_date))
        for i in Library.books:
            if i.book_id == book_id:
                if i.available == False:
                    print("There is no book available")
                    break
                i.available = False
                print("you borrow the book successfully")
    

    def returnBook(self,book_id,start_date,cur_date):
        Library.records.append((self.user_id,book_id,start_date,cur_date))
        for i in Library.books:
            if i.book_id == book_id:
                i.available = True
                print("Book returned successfully")
        
    







    
    
