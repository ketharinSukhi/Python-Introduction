import csv


class Book:

    FILE_NAME = "book.csv"

    def __init__(self, book_name):
        
        self.name = book_name

    @staticmethod
    def add(name):
        with open("Book.FILE_NAME", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name])
        print(f"{name} Book is added in the list")



    @staticmethod
    def update(old_name, new_name):
        books = []
        updated = False
        with open("Book.FILE_NAME", "r", newline="") as file:
           reader = csv.reader(file)
           for row in reader:
                if row and row[0] == old_name:
                    #replace old name with new name
                    books.append([new_name])
                    updated = True
                else:
                    books.append(row)

        # write back the updated list to the file
        if updated:
            with open("Book.FILE_NAME", "r", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(books)
            print(f'"{old_name}" has been updated to "{new_name}".')
        else:
            print(f'Book "{old_name}" not found.')



    @staticmethod
    def delete():
        print("Book is deleted from the list")
    @staticmethod
    def search_contacts():
        print("Book is searching in the list")
    @staticmethod
    def options(criteria):
      match criteria:
        case 1:
             name = input("Enter the book name for add: ")
             name = Book.add(name)
             return name
        case 2:
            old_name = input("Enter the current book name: ")
            new_name = input("Enter the new book name: ")
            name = Book.update()
            return name
        case 3:

            name = input("Enter the book name for update: ")
            name = Book.delete()
            return name
        case 4:
            name = input("Enter the book name for update: ")
            name = Book.search_contacts()
            return name
        case _:
              print("Invalid")

def main():
   print("Choose:")
   print(" 1 for add books\n 2 for update books \n 3 for delete books \n 4 for search contacts")

   criteria = int(input("Enter your number: "))
   Book.options(criteria)
                    

if __name__ == "__main__":
    main()
