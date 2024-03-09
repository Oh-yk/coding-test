import sys
input = sys.stdin.readline

board = [[0] * 20]
for _ in range(19):
    row = [0]
    row.extend(list(map(int, input().split())))
    board.append(row)

lines = [[(0, 1), (0, 2), (0, 3), (0, 4)],
    [(1, 1), (2, 2), (3, 3), (4, 4)],
    [(1, 0), (2, 0), (3, 0), (4, 0)],
    [(1, -1), (2, -2), (3, -3), (4, -4)]]

game_end = False
for r in range(1, 20):
    if game_end:
        break
    for c in range(1, 20):
        if game_end:
            break
        if board[r][c] == 0:
            continue
        if board[r][c] == 1:
            for type, line in enumerate(lines):
                end_r = r + line[-1][0]
                end_c = c + line[-1][1]
                if end_r > 19 or end_r < 1 or end_c > 19 or end_c < 1:
                    continue
                if board[r + line[0][0]][c + line[0][1]] == 1 and board[r + line[1][0]][c + line[1][1]] == 1 \
                    and board[r + line[2][0]][c + line[2][1]] == 1 and board[r + line[3][0]][c + line[3][1]] == 1:
                    game_end = True 
                    print("1")
                    if type == 3:
                        print(f"{r + line[3][0]} {c + line[3][1]}")
                    else:
                        print(f"{r} {c}")
                    break
        if board[r][c] == 2:
            for type, line in enumerate(lines):
                end_r = r + line[-1][0]
                end_c = c + line[-1][1]
                if end_r > 19 or end_r < 1 or end_c > 19 or end_c < 1:
                    continue
                if board[r + line[0][0]][c + line[0][1]] == 2 and board[r + line[1][0]][c + line[1][1]] == 2 \
                    and board[r + line[2][0]][c + line[2][1]] == 2 and board[r + line[3][0]][c + line[3][1]] == 2:
                    game_end = True 
                    print("2")
                    if type == 3:
                        print(f"{r + line[3][0]} {c + line[3][1]}")
                    else:
                        print(f"{r} {c}")
                    break

if not game_end:
    print("0")
        
    
    
    
