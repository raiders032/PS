'''
16940번 BFS 스페셜 저지 골드4
'''
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)


def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    level = 1
    while q:
        v = q[0]
        q.popleft()
        for w in range(len(graph[v])):
            nv = graph[v][w]
            if visited[nv] > 0:
                continue
            visited[nv] = level + 1
            q.append(nv)
        level += 1


for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
bfs()
ans = list(map(int, input().split()))
level = 1
for i in range(N):
    if visited[ans[i]] == level or visited[ans[i]] == level + 1:
        if visited[ans[i]] == level + 1:
            level += 1
    else:
        print(0)
        break

else:
    print(1)
