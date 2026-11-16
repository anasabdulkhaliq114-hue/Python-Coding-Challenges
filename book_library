library = []
your_books = input("enter the name of a book you own: ").lower()
library.append(your_books)

your_books1 = input("enter another book you own (or press enter to skip): ").lower()
if your_books1:
    library.append(your_books1)
    print(f"your library: {library}")
else:
    print(f"your library: {library}")

library_wish = []

your_wish = input("enter the name of a book you wish to have in the future: ").lower()
library_wish.append(your_wish)

your_wish1 = input("enter the name of another book you wish to have in the future (or press enter to skip): ").lower()
if your_wish1:
    library_wish.append(your_wish1)
    print(f"your wish library: {library_wish}")
else:
    print(f"your wish library: {library_wish}")

book1 = input("enter the name of a book from your wish library that you got (or press enter to skip): ").lower()
if book1 in library_wish:
    library_wish.remove(book1)
    library.append(book1)
    print(f"updated library: {library}")
    print(f"updated wish library: {library_wish}")
else:
    print(f"updated wish library: {library_wish}")

book2 = input("enter the name of a book from your library you wish to donate (or press enter to skip): ").lower()
if book2 in library:
    library.remove(book2)
    print(f"final library after donations: {library}")
else:
    print(f"final library after donations: {library}")
