directory = {}

print("Enter name of directory -- CSE")
while True:
    print("1. Create File 2. Delete File 3. Search File")
    print("4. Display Files 5. Exit")
    choice = int(input("Enter your choice – "))

    if choice == 1:
        name = input("Enter the name of the file -- ")
        if name in directory:
            print(f"Error: File '{name}' already exists.")
        else:
            directory[name] = ""
            print(f"File '{name}' created successfully.")
    elif choice == 2:
        name = input("Enter the name of the file – ")
        if name in directory:
            del directory[name]
            print(f"File '{name}' is deleted")
        else:
            print(f"Error: File '{name}' not found.")
    elif choice == 3:
        name = input("Enter the name of the file – ")
        if name in directory:
            print(f"File '{name}' found")
        else:
            print(f"File '{name}' not found")
    elif choice == 4:
        if not directory:
            print("No files in the directory.")
        else:
            print("The Files are -- ", end="")
            print(" ".join(directory.keys()))
    elif choice == 5:
        break
    else:
        print("Invalid choice, please try again.")
