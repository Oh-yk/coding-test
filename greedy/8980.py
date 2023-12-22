# N, capacity = list(map(int, input().split()))
# M = int(input())
# send_list = []
# for _ in range(M):
#     info = tuple(map(int, input().split()))
#     send_list.append(info)

test_case = open("./8980_1.txt", "r")
lines = test_case.readlines()

N, capacity = map(int, lines[0].split())
M = int(lines[1])
send_list = []
for line in lines[2:]:
    info = tuple(map(int, line.split()))
    send_list.append(info)
    
send_list.sort(key=lambda info: (-info[1], -info[0]))

total = 0
current_num = 0
current_stat = []

# info[2]: number of packages
for info in send_list:
    current_vilage = info[1]
    for curr_info in current_stat:
        if curr_info[0] == current_vilage:
            current_num -= curr_info[2]
            current_stat.remove(curr_info)
    if current_num < capacity:
        pick_up = min(capacity - current_num, info[2])
        current_num += pick_up
        total += pick_up
        current_stat.append((info[0], info[1], pick_up))

print(total)