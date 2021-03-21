N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
res = 0
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)


def dfs(v):
    global res
    if v == N:
        res += 1
        return
    for i in range(len(graph[v])):
        if visited[graph[v][i]] == False:
            visited[graph[v][i]] = True
            dfs(graph[v][i])
            visited[graph[v][i]] = False


visited[1] = True
dfs(1)
print(res)
