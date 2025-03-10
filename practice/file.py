name = input("Enter name: ")

# Writing to the file (Overwrites existing content)**
with open("file.txt","a") as file:
 file.write(f"{name}\n")
with open("file.txt","r") as file: 
    for line in file:
      print("hello, " ,line.rstrip())
