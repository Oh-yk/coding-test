import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trains = ["x"]
trains.extend(["X00000000000000000000"] * N)
for _ in range(M):
    command = list(map(int, input().split()))
    command_type = command[0]
    train_num = command[1]
    if command_type in [1, 2]:
        seat_num = command[2]
    if command_type == 1:
        trains[train_num] = trains[train_num][:seat_num] + "1" + trains[train_num][seat_num+1:]
    if command_type == 2:
        trains[train_num] = trains[train_num][:seat_num] + "0" + trains[train_num][seat_num+1:]
    if command_type == 3:
        trains[train_num] = "X0" + trains[train_num][1:-1]
    if command_type == 4:
        trains[train_num] = "X" + trains[train_num][2:] + "0"

tot = len(set(trains[1:]))
print(tot)
