T = int(input())

for _ in range(T):
    n, d = map(int, input().split())
    array = [[0] * (n + 1)]
    for _ in range(n):
        row = [0]
        row.extend(list(map(int, input().split())))
        array.append(row)
    
    rot = d // 45
    step = n // 2
    center = (n+1)//2
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    
    for s in range(1, step + 1):
        original = []
        for dx, dy in neighbors:
            dx = dx * s
            dy = dy * s
            original.append(array[center + dx][center + dy])
        for i, (dx, dy) in enumerate(neighbors):
            dx = dx * s
            dy = dy * s
            array[center + dx][center + dy] = original[(i-rot) % 8]
            
    for r in range(1, n+1):
        print(" ".join(map(str, array[r][1:])))
            
        
        
    
    
    