from lis import books


def add_book():
   
    name = input("\nEnter the name of book: ")
    books.append(name)
    print()
    print(name,"is added successfully.")