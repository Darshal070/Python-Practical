# FCFS CPU Scheduling Algorithm

n = int(input("Enter number of processes: "))

processes = []
burst_time = []

for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append(f"P{i+1}")
    burst_time.append(bt)

waiting_time = [0] * n
turnaround_time = [0] * n

# Calculate Waiting Time
for i in range(1, n):
    waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

# Calculate Turnaround Time
for i in range(n):
    turnaround_time[i] = waiting_time[i] + burst_time[i]

print("\nProcess\tBT\tWT\tTAT")

total_wt = 0
total_tat = 0

for i in range(n):
    print(f"{processes[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")
    total_wt += waiting_time[i]
    total_tat += turnaround_time[i]

print("\nAverage Waiting Time =", total_wt / n)
print("Average Turnaround Time =", total_tat / n)
