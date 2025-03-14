import csv
class ToDoList:
    file_name = "Task.csv"
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = []

        
    def add_tasks(self, task_description):
        
        print("")

    def mark_task_completed(self):
        print("")

    def delete_task(self):
        print("")

    def save_task(self):
        print("")

    def show_task(self.):

       

    @staticmethod
    def options(criteria):
      match criteria:
        case 1:
            task = input("Enter task description: ")
            ToDoList.add_tasks(task)
            
        case 2:
            mark_task_completed()
            
        case 3:
            delete_task()
            
        case 4:
            save_task()
             
        case _:
              print("Invalid")

def main():
   print("Choose:")
   print(" 1 for add books\n "
   "2 for update books \n "
   "3 for delete books \n "
   "4 for search contacts")
   criteria = int(input("Enter your number: "))
   Book.options(criteria)
                    

if __name__ == "__main__":
    main()
    


        