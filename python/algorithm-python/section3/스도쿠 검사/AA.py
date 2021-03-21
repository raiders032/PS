board = [list(map(int, input().split())) for _ in (range(9))]

for r in board:
    visited = [False] * 10
    for x in r:
        if visited[x]:
            print("NO")
            exit(0)
        visited[x] = True

for c in range(9):
    for r in range(9):
        visited = [False] * 10
        if visited[board[r][c]]:
            print("NO")
            exit(0)
        visited[board[r][c]] = True

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        visited = [False] * 10
        for r in range(i, i+3):
            for c in range(j, j+3):
                if visited[board[r][c]]:
                    print("NO")
                    exit(0)
                visited[board[r][c]] = True
print("YES")
