N = int(input())
board = [list() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
min_h = 1000000000
max_h = 0
start = (0, 0)
end = (N-1, N-1)
res = 0


def dfs(x, y):
    global res
    if x == end[0] and y == end[1]:
        res += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny] or board[x][y] >= board[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny)
        visited[nx][ny] = False


for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] < min_h:
            min_h = row[j]
            start = (i, j)
        if row[j] > max_h:
            max_h = row[j]
            end = (i, j)
        board[i].append(row[j])

visited[start[0]][start[1]] = True
dfs(start[0], start[1])
print(res)
