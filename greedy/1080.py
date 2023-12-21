N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    row = list(map(int, input()))
    A.append(row)
for _ in range(N):
    row = list(map(int, input()))
    B.append(row)

same = True
Diff = []
for r in range(N):
    row = []
    for c in range(M):
        if A[r][c] != B[r][c]:
            row.append(True)
            same = False
        else:
            row.append(False)
    Diff.append(row)

def main():
    # Matrix가 3*3 보다 작을 때
    if N < 3 or M < 3:
        if same:
            return 0
        else:
            return -1
        
    count = 0
    # Matrix가 3*3 이상일 때
    for r in range(N-2):
        for c in range(M-2):
            if Diff[r][c] == True:
                # 연산 수행
                for k in range(3):
                    for l in range(3):
                        Diff[r+k][c+l] = not Diff[r+k][c+l]
                count += 1
        if Diff[r][-1] or Diff[r][-2]:
            return -1
    
    for r in range(N):
        for c in range(M):
            if Diff[r][c]:
                return -1
    
    return count

print(main())
            
                    
        
