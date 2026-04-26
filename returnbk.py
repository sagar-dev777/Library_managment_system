from lis import books, issued_book

def return_book():
    print()
    name = input("Enter the name of book you borrowed: ")
    if name in issued_book:
        issued_book.remove(name)
        books.append(name)
        print()
        print(name,"is returned successfully.\n")
    else:
        print()
        print(name, "is not issued\n")