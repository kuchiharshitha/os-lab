def mft(total_memory, block_size, process_sizes):
    blocks = total_memory // block_size
    internal_frag = external_frag = 0

    print("PROCESS ALLOCATED MEMORY REQUIRED INTERNAL FRAGMENTATION")
    for i, size in enumerate(process_sizes, 1):
        if size <= block_size and blocks > 0:
            internal_frag += block_size - size
            external_frag -= block_size
            print(f"{i} {size} YES {block_size - size}")
            blocks -= 1
        else:
            print(f"{i} {size} NO -----")

    print(f"\nMemory is Full, Remaining Processes cannot be accommodated")
    print(f"Total Internal Fragmentation is {internal_frag}")
    print(f"Total External Fragmentation is {external_frag}")

# Input
total_memory = int(input("Enter the total memory available (in Bytes): "))
block_size = int(input("Enter the block size (in Bytes): "))
process_sizes = [int(input(f"Enter memory required for process {i+1} (in Bytes): ")) for i in range(int(input("Enter the number of processes: ")))]

mft(total_memory, block_size, process_sizes)
