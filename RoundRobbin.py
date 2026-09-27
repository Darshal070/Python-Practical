# Round Robin CPU Scheduling Algorithm

n = int(input("Enter number of processes: "))

processes = []
burst_time = []

for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append(f"P{i+1}")
    burst_time.append(bt)

quantum = int(input("Enter Time Quantum: "))

remaining_time = burst_time.copy()
waiting_time = [0] * n
turnaround_time = [0] * n

time = 0

while True:
    done = True

    for i in range(n):
        if remaining_time[i] > 0:
            done = False

            if remaining_time[i] > quantum:
                time += quantum
                remaining_time[i] -= quantum
            else:
                time += remaining_time[i]
                waiting_time[i] = time - burst_time[i]
                remaining_time[i] = 0

    if done:
        break

# Calculate Turnaround Time
for i in range(n):
    turnaround_time[i] = burst_time[i] + waiting_time[i]

print("\nProcess\tBT\tWT\tTAT")

total_wt = 0
total_tat = 0

for i in range(n):
    print(f"{processes[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")
    total_wt += waiting_time[i]
    total_tat += turnaround_time[i]

print("\nAverage Waiting Time =", total_wt / n)
print("Average Turnaround Time =", total_tat / n)
