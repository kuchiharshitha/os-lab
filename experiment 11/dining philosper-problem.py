import itertools

def dining_philosophers():
    total_philosophers = int(input("DINING PHILOSOPHER PROBLEM\nEnter the total no. of philosophers: "))
    hungry_positions = [int(input(f"Enter philosopher {i+1} position: ")) for i in range(int(input("How many are hungry: ")))]

    while (choice := input("\n1. One can eat at a time\n2. Two can eat at a time\n3. Exit\nEnter your choice: ")) != "3":
        if choice == "1":
            print("Allow one philosopher to eat at any time")
            for p in hungry_positions:
                print(f"P {p} is granted to eat")
                print(''.join(f"P {x} is waiting\n" for x in hungry_positions if x != p))
        elif choice == "2":
            print("Allow two philosophers to eat at the same time")
            for i, (p1, p2) in enumerate(itertools.combinations(hungry_positions, 2), 1):
                print(f"Combination {i}\nP {p1} and P {p2} are granted to eat")
                print(''.join(f"P {x} is waiting\n" for x in hungry_positions if x != p1 and x != p2))
        else:
            print("Invalid choice.")

dining_philosophers()
