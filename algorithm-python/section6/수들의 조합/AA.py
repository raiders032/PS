N, M = map(int, input().split())
arr = list(map(int, input().split()))
target = int(input())
res = 0


def dfs(cnt, idx, total):
    global res
    if cnt == M:
        if total % target == 0:
            res += 1
        return
    for i in range(idx, N):
        dfs(cnt+1, i+1, total + arr[i])


dfs(0, 0, 0)
print(res)
