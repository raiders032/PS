from collections import deque
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
start = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0


def bfs():
    q = deque()
    for x, y in start:
        visited[x][y] = 1
        q.append((x, y))
    while q:
        x = q[0][0]
        y = q[0][1]
        q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] or board[nx][ny] != 0:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            start.append((x, y))

bfs()

for x in range(N):
    for y in range(M):
        if visited[x][y] == 0 and board[x][y] == 0:
            print(-1)
            exit(0)
        res = max(res, visited[x][y])
print(res-1)
