N = int(input())
T = [0]
P = [0]
res = 0


def dfs(day, pay):
    global res
    if day > N:
        res = max(res, pay)
        return
    else:
        if day + T[day] <= N+1:
            dfs(day + T[day], pay + P[day])
        dfs(day + 1, pay)


for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
dfs(1, 0)
print(res)
