li = list(map(int, input("Enter page numbers: ").split()))
si = int(input("Enter Size: "))
li1 = [-1] * si
lru_counter = [0] * si
co = 0

for idx, i in enumerate(li):
    if i in li1:
        lru_counter[li1.index(i)] = idx
    else:
        if -1 in li1:
            empty_index = li1.index(-1)
            li1[empty_index] = i
            lru_counter[empty_index] = idx
        else:
            lru_index = lru_counter.index(min(lru_counter))
            li1[lru_index] = i
            lru_counter[lru_index] = idx
        co += 1
    
    for j in li1:
        print(j, end=" ")
    print()
    
print("Number of faults = ", co)
