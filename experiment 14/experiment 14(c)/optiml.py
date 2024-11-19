# Input
pages = list(map(int, input("Enter page numbers: ").split()))
size = int(input("Enter Size: "))

# Initialize memory and faults
memory = [-1] * size
page_faults = 0

# Process each page
for i, page in enumerate(pages):
    if page not in memory:
        future_use = [(pages[i+1:].index(m) if m in pages[i+1:] else float('inf')) for m in memory]
        memory[memory.index(-1) if -1 in memory else future_use.index(max(future_use))] = page
        page_faults += 1
    print(" ".join(map(str, memory)))

print("No of faults =", page_faults)
