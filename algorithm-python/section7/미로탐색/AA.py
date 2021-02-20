board = [list(map(int, input().split())) for _ in range(7)]
visited = [[False] * 7 for _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0


def dfs(x, y):
    global res
    if x == 6 and y == 6:
        res += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 7 or ny < 0 or ny >= 7:
            continue
        if visited[nx][ny] or board[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny)
        visited[nx][ny] = False


visited[0][0] = True
dfs(0, 0)
print(res)
