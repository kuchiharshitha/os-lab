num_blocks, num_files = int(input("Enter the number of blocks: ")), int(input("Enter the number of files: "))
blocks = sorted([(int(input(f"Block {i+1}: ")), i+1) for i in range(num_blocks)], key=lambda x: x[0])
files = [int(input(f"File {i+1}: ")) for i in range(num_files)]

print("File No File Size Block No Block Size Fragment")
for f_no, f_size in enumerate(files, 1):
    best = min((b for b in blocks if b[0] >= f_size), default=None, key=lambda x: x[0] - f_size)
    if best:
        blocks.remove(best)
        print(f"{f_no} {f_size} {best[1]} {best[0]} {best[0] - f_size}")
