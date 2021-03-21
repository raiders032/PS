from collections import deque

N, M = map(int, input().split())
visited = [False] * (N+1)
visited_num = []


def dfs(cnt):
    if cnt >= N:
        q = deque(visited_num)
        length = len(q)
        for i in range(length - 1):
            for _ in range(i, length - 1):
                q.append(q.popleft() + q[0])
            q.popleft()
        if q[0] == M:
            for x in visited_num:
                print(x, end=' ')
            exit(0)
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        visited_num.append(i)
        dfs(cnt+1)
        visited[i] = False
        visited_num.pop()


dfs(0)
