def fcfs():
    n = int(input("Enter the number of Jobs: "))
    bt = []
    wt = [0] * n
    tat = [0] * n
    for i in range(n):
        burst_time = int(input(f"Enter Burst Time for Jobs {i}: "))
        bt.append(burst_time)
    wt[0] = 0
    tat[0] = bt[0]
    wtavg = 0
    tatavg = bt[0]
    for i in range(1, n):
        wt[i] = wt[i-1] + bt[i-1]
        tat[i] = tat[i-1] + bt[i]
        wtavg += wt[i]
        tatavg += tat[i]
    print("\t JOB \tBURST TIME \t WAITING TIME\t TURNAROUND TIME")
    for i in range(n):
        print(f"\n\t J{i} \t\t {bt[i]} \t\t {wt[i]} \t\t {tat[i]}")
    print("\nAverage Waiting Time --", wtavg/n)
    print("\nAverage Turnaround Time --", tatavg/n)
fcfs()
