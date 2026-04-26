from add import add_book
from show import show_books
from issue import borrow_book
from returnbk import return_book





def library():
    while True:
        print("\n\n")
        
        print("|" + "-"*26 + "|")
        print("|--WELCOME TO CGC LIBRARY--|")
        print("|--------------------------|")
        print("|--------- Menu :----------|")
        print("|---- 1. Add book ---------|")
        print("|---- 2. Show books -------|")
        print("|---- 3. Borrow book ------|")
        print("|---- 4. Return books -----|")
        print("|-----5. Exit -------------|")
        print("|"+"-"*26 + "|\n")
        choice = int(input("Enter the choice: "))
        
        if choice == 1:
            add_book()
            
        elif choice == 2:
            show_books()
            
        elif choice == 3:
            borrow_book()
            
        elif choice == 4:
            return_book()
            
        elif choice == 5:
            print("\nThank-you  Visit again.")
            print()
            break
        
        else:
            print("\nInvalid choice")
            
library()