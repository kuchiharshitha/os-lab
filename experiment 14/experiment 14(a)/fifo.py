li = list(map(int,input("Enter page numbers:").split()))
si = int(input("Enter Size :"))
li1 = [-1]*si
co = 0
for i in li:
    if i not in li1:
        li1[co%si]=i
        co+=1
    for j in li1:
        print(j,end=" ")
    print()
print("No of faults = ",co)
