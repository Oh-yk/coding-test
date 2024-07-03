import sys
input = sys.stdin.readline

wheels = [[]]
for _ in range(4):
    line = list(map(int, list(input().strip())))
    wheels.append(line)
    
K = int(input())
commands = []
for _ in range(K):
    line = list(map(int, input().split()))
    commands.append(line)

def different(a, b):
    if a < b:
        return wheels[a][2] != wheels[b][6]
    else:
        return wheels[b][2] != wheels[a][6]

def rotate(wheel, dir):
    if dir == 0:
        return
    if dir == 1:
        wheels[wheel] = [wheels[wheel][-1]] + wheels[wheel][:-1]
    if dir == -1:
        wheels[wheel] = wheels[wheel][1:] + [wheels[wheel][0]]

for k in range(K):
    rot_wheel, rot_dir = commands[k]
    rot_info = [0, 0, 0, 0, 0]
    
    if rot_wheel == 1:
        rot_info[1] = rot_dir
        if different(1, 2):
            rot_info[2] = -rot_dir
            if different(2, 3):
                rot_info[3] = rot_dir
                if different(3, 4):
                    rot_info[4] = -rot_dir
                    
    elif rot_wheel == 2:
        rot_info[2] = rot_dir
        if different(1, 2):
            rot_info[1] = -rot_dir
        if different(2, 3):
            rot_info[3] = -rot_dir
            if different(3, 4):
                rot_info[4] = rot_dir
    
    elif rot_wheel == 3:
        rot_info[3] = rot_dir
        if different(3, 4):
            rot_info[4] = -rot_dir
        if different(2, 3):
            rot_info[2] = -rot_dir
            if different(1, 2):
                rot_info[1] = rot_dir
    
    else:
        rot_info[4] = rot_dir
        if different(4, 3):
            rot_info[3] = -rot_dir
            if different(3, 2):
                rot_info[2] = rot_dir
                if different(2, 1):
                    rot_info[1] = -rot_dir
                    
    for i in range(1, 5):
        rotate(i, rot_info[i])

ans = wheels[1][0] * 1 + wheels[2][0] * 2 + wheels[3][0] * 4 + wheels[4][0] * 8
print(ans)
    