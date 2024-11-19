num_blocks, num_files = int(input("Enter the number of blocks: ")), int(input("Enter the number of files: "))

block_sizes = [int(input(f"Block {i+1}: ")) for i in range(num_blocks)]
file_sizes = [int(input(f"File {i+1}: ")) for i in range(num_files)]

blocks = sorted([(size, i+1) for i, size in enumerate(block_sizes)], key=lambda x: x[0])
allocations = []

for file_no, file_size in enumerate(file_sizes, 1):
    best_block = min(((bsize, bno) for bsize, bno in blocks if bsize >= file_size), default=None, key=lambda x: x[0] - file_size)
    if best_block:
        blocks.remove(best_block)
        allocations.append((file_no, file_size, best_block[1], best_block[0], best_block[0] - file_size))

print("File No File Size Block No Block Size Fragment")
for alloc in allocations:
    print(f"{alloc[0]} {alloc[1]} {alloc[2]} {alloc[3]} {alloc[4]}")
