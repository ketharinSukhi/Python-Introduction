import csv


class Book:

    def __init__(self, book_name):
        
        self.name = book_name


    def add():

        print("Book is added in the list")

    def update():
        print("Book is updated in the list")

    def delete():
        print("Book is deleted in the list")

    def search_contacts():
        print("Book is searching in the list")

    def options(criteria):
      match criteria:
        case 1:
             name = input("Enter the book name for add")
             name = Book.add()
             return name
        case 2:
            name = input("Enter the book name for update")
            name = Book.update()
            return name
        case 3:
            name = input("Enter the book name for update")
            name = Book.delete()
            return name
        case 4:
            name = input("Enter the book name for update")
            name = Book.search_contacts()
            return name

def main():
   print("Choose:")
   print(" 1 for add books\n 2 for update books \n 3 for delete books \n 4 for search contacts")

   criteria = int(input("Enter your number: "))
   Book.options(criteria)
            
        

if __name__ == "__main__":
    main()
