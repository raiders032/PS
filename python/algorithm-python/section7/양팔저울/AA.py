N = int(input())
arr = list(map(int, input().split()))
isOk = [False] * (sum(arr)+1)


def dfs(l, sum):
    if l >= N:
        if sum > 0:
            isOk[sum] = True
        return
    else:
        dfs(l+1, sum + arr[l])
        dfs(l+1, sum)
        dfs(l+1, sum - arr[l])


dfs(0, 0)
cnt = 0
for x in isOk:
    if x == False:
        cnt += 1
print(cnt-1)
