C, N = map(int, input().split())
w = []
sum_w = 0
max_w = 0


def dfs(idx, sum):
    global max_w
    if idx >= N:
        return
    if sum_w - sum <= C:
        max_w = max(max_w, sum_w - sum)
    if sum_w - sum < max_w:
        return
    dfs(idx+1, sum + w[idx])
    dfs(idx+1, sum)


for _ in range(N):
    num = int(input())
    w.append(num)
    sum_w += num
dfs(0, 0)
print(max_w)
