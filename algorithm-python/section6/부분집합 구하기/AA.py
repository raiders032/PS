def DFS(idx):
    if idx > n:
        for i in range(1, n+1):
            if visited[i]:
                print(i, end=' ')
        print()
        return
    else:
        visited[idx] = True
        DFS(idx + 1)
        visited[idx] = False
        DFS(idx + 1)


n = int(input())
visited = [False] * (n + 1)
DFS(1)
