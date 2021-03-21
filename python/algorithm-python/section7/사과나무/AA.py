from collections import deque

N = int(input())
visited = [[0] * N for _ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0


def bfs(x, y):
    global res
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x = q[0][0]
        y = q[0][1]
        q.popleft()
        res += board[x][y]
        if visited[x][y] > N // 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


bfs(N//2, N//2)
print(res)
