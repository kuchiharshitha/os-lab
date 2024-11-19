class SequentialAllocation:
    def __init__(self, disk_size):
        self.disk_size = disk_size
        self.disk = [None] * disk_size

    def allocate_file(self, start_block, length):
        if start_block + length > self.disk_size:
            print("Error: Not enough space to allocate the file.")
            return

        for i in range(start_block, start_block + length):
            if self.disk[i] is not None:
                print("Error: Block already occupied.")
                return

        for i in range(start_block, start_block + length):
            self.disk[i] = '1'
            print(f"{i}->{1}")
        
        print("The file is allocated to disk")

    def display_disk(self):
        print("Disk Blocks:", self.disk)


# Example usage
disk = SequentialAllocation(20)
start_block = int(input("Enter the starting block: "))
length = int(input("Enter the length of the file: "))
disk.allocate_file(start_block, length)
disk.display_disk()
