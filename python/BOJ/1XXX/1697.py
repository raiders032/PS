"""
1697.숨바꼭질
실버1
BFS, 그래프이론, 그래프탐색
"""
from collections import deque


def bfs(cur_v):
    visited[cur_v] = 1
    q = deque()
    q.append(cur_v)
    while q:
        cur_v = q.popleft()
        if cur_v == K:
            return visited[K] - 1
        if cur_v - 1 >= 0 and not visited[cur_v - 1]:
            visited[cur_v - 1] = visited[cur_v] + 1
            q.append(cur_v - 1)
        if cur_v + 1 <= 100000 and not visited[cur_v + 1]:
            visited[cur_v + 1] = visited[cur_v] + 1
            q.append(cur_v + 1)
        if 2 * cur_v <= 100000 and not visited[2 * cur_v]:
            visited[2 * cur_v] = visited[cur_v] + 1
            q.append(2 * cur_v)


N, K = map(int, input().split())
visited = [0] * 100001
print(bfs(N))
