res = 0
arr = []


def dfs(l):
    if l >= M:
        global res
        res += 1
        for x in arr:
            print(x, end=' ')
        print()
        return
    for i in range(1, N+1):
        arr.append(i)
        dfs(l+1)
        arr.pop()


N, M = map(int, input().split())
dfs(0)
print(res)
