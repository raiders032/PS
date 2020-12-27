N = int(input())
board = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
res = []


def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny] or not board[nx][ny]:
            continue
        dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if board[i][j] and not visited[i][j]:
            dfs(i, j)
            res.append(cnt)
            cnt = 0

res.sort()
print(len(res))
for x in res:
    print(x)
