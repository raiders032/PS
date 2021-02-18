from collections import deque
board = [list(map(int, input().split())) for _ in range(7)]
visited = [[0] * 7 for _ in range(7)]
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
        if x == 6 and y == 6:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 7 or ny < 0 or ny >= 7:
                continue
            if visited[nx][ny] or board[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


bfs(0, 0)
print(visited[6][6] - 1)
