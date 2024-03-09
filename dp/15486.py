import sys
input = sys.stdin.readline

N = int(input())
income = [0]

for _ in range(N):
    period, money = map(int, input().split())
    income.append((period, money))

max_income = [-1] * (N + 1)
for day in range(N, 0, -1):
    if day == N:
        if income[day][0] == 1:
            max_income[day] = income[day][1]
            continue
        else:
            max_income[day] = 0
            continue
    
    end = day + income[day][0] - 1
    if end > N:
        max_income[day] = max_income[day + 1]
    elif end == N:
        max_income[day] = max(income[day][1], max_income[day + 1])
    else:
        max_income[day] = max(income[day][1] + max_income[day + income[day][0]], max_income[day + 1])

print(max_income[1])