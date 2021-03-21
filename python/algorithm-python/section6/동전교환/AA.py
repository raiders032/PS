N = int(input())
coin = list(map(int, input().split()))
num = int(input())
min_cnt = 1000000


def dfs(cnt, sum):
    global min_cnt
    if sum > num:
        return
    if cnt > min_cnt:
        return
    if sum == num:
        min_cnt = min(min_cnt, cnt)
        return
    for i in range(N):
        dfs(cnt + 1, sum + coin[i])


coin.sort(reverse=True)
dfs(0, 0)
print(min_cnt)
