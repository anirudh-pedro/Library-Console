from app import Library

class Records:
    def __init__(self,user_id,book_id,start_date,end_date):
        self.user_id = user_id
        self.book_id = book_id
        self.start_date = start_date
        self.end_date = end_date
        Library.records.append((user_id,book_id,start_date,end_date))
    
    def ShowRecords(self):
        for r in Library.records:
            print(r.user_id, r.book_id, r.start_date, r.end_date)
    
    def ShowRecords_id(self,user_id):
        for r in Library.records:
            if r.user_id == user_id:
                print(r.user_id, r.book_id, r.start_date, r.end_date)
        
    

    
    

        