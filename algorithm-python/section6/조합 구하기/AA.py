N, M = map(int, input().split())
arr = []
res = 0


def dfs(idx, cnt):
    global res
    if cnt == M:
        res += 1
        for x in arr:
            print(x, end=' ')
        print()
        return
    for i in range(idx+1, N+1):
        arr.append(i)
        dfs(i, cnt+1)
        arr.pop()


dfs(0, 0)
print(res)
