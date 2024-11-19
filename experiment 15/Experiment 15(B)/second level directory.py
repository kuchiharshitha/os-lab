directory_structure = {}
print("1. Create Directory 2. Create File 3. Delete File 4. Search File 5. Display 6. Exit")
while True:
    choice = int(input("Enter your choice -- "))
    if choice == 1:
        dir_name = input("Enter name of directory -- ")
        if dir_name in directory_structure:
            print("Directory already exists.")
        else:
            directory_structure[dir_name] = []
            print(f"Directory '{dir_name}' created")
    elif choice == 2:
        dir_name = input("Enter name of the directory – ")
        if dir_name not in directory_structure:
            print("Directory not found.")
        else:
            file_name = input("Enter name of the file -- ")
            directory_structure[dir_name].append(file_name)
            print(f"File '{file_name}' created")
    elif choice == 3:
        dir_name = input("Enter name of the directory – ")
        if dir_name not in directory_structure:
            print("Directory not found.")
        else:
            file_name = input("Enter name of the file – ")
            if file_name in directory_structure[dir_name]:
                directory_structure[dir_name].remove(file_name)
                print(f"File '{file_name}' is deleted")
            else:
                print("File not found.")
    elif choice == 4:
        file_name = input("Enter the name of the file – ")
        found = False
        for dir_name, files in directory_structure.items():
            if file_name in files:
                print(f"File '{file_name}' found in directory '{dir_name}'")
                found = True
                break
        if not found:
            print("File not found")
    elif choice == 5:
        if not directory_structure:
            print("No directories available.")
        else:
            for dir_name, files in directory_structure.items():
                print(f"Directory '{dir_name}': {' '.join(files) if files else 'No files'}")
    elif choice == 6:
        break
    else:
        print("Invalid choice, please try again.")
