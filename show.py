from lis import books



def show_books():
    
    if len(books) == 0:
        print("No books available")
    else:
        print("\nAvailabel Books :->")
        print()
        for j in range(len(books)):
          print(j+1, ":", books[j])