from lis import books, issued_book



def borrow_book():
   
    name = input("\nEnter the name of book that you want to borrow : ")
    
    if name in books:
       issued_book.append(name)
       books.remove(name)
       print()
       print(name,"is issued successfully.")
    else:
        print()
        print(name,"is not available in library.")