from Librarian import Librarian
from user import Student

from app import Library
li = [("Harry potter",1),("Harry",2),("potter",3),("Harry pot",4),("rry potter",5)]
obj = Librarian("Anirudh",101)
for i in range(len(li)):
    obj.addBooks(li[i][0],li[i][1])
obj.addBooks("Harry potter",1)

for i in Library.books:
    print(i.book_name,end = " ")
    print(i.book_id)
    print()


nam = [("anirudh","A1","anirudh200503@gmail.com"),("ani","A2","anirudh2003@gmail.com"),("anir","A3","udh200503@gmail.com"),("anir","A4","anirudh2005@gmail.com"),("an","A5","anirudh03@gmail.com"),("anirudh_pedro","A6","anir@gmail.com"),("ani_pedro","A7","dh200503@gmail.com")]

for i in nam:
    obj = Student(i[0],i[1],i[2])

for i in Library.users:
    print(i.user_id, i.name, i.email)
    print()



while True:
    print("Enter 1 for Register as a user")
    print("Enter 2 for Login")
    print("Enter 3 for exit")
    inp = int(input())
    if inp == 3:
        print("Thank you")
        break
    elif inp == 1:
        print("Enter your name")
        name = input()
        print("Enter your user_id")
        user_id = input()
        print("Email")
        email = input()
        flag = 0
        for i in Library.users:
            if i.email == email:
                print("user already registered")
                flag = 1
                break
        if flag == 0:
            obj = Student(name,user_id,email)
    elif inp == 2:
        print("enter 1 for login as Librarian")

