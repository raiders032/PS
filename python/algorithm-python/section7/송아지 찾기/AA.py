from collections import deque
S, E = map(int, input().split())
visited = [0] * (10001)
dx = [1, -1, 5]


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == E:
            return
        for i in range(3):
            nx = x + dx[i]
            if nx < 1 or nx > 10000:
                continue
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)


bfs(S)
print(visited[E] - 1)
