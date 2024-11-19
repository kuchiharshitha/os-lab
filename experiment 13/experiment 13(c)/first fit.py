num_blocks, num_files = int(input("Enter the number of blocks: ")), int(input("Enter the number of files: "))
blocks = [(int(input(f"Block {i+1}: ")), i+1) for i in range(num_blocks)]
files = [int(input(f"File {i+1}: ")) for i in range(num_files)]

print("File No File Size Block No Block Size Fragment")
for f_no, f_size in enumerate(files, 1):
    for b_index, (b_size, b_no) in enumerate(blocks):
        if b_size >= f_size:
            print(f"{f_no} {f_size} {b_no} {b_size} {b_size - f_size}")
            blocks.pop(b_index)  # Remove the block after allocation
            break
