# N = int(input())
# schedules = []
# for i in range(N):
#     start, end = map(int, input().split())
#     schedules.append((start, end))

test_case = open("./1931.txt", "r")
lines = test_case.readlines()
N = int(lines[0].strip())
schedules = []
for line in lines[1:]:
    start, end = [int(t) for t in line.strip().split()]
    schedules.append((start, end))
    
schedules.sort(key = lambda x: (x[1], x[0]))

total = 1
time_bar = schedules[0][1]
for schedule in schedules[1:]:
    if schedule[0] >= time_bar:
        time_bar = schedule[1]
        total += 1

print(total)
        
        
    