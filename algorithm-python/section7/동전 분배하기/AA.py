N = int(input())
C = [int(input()) for _ in range(N)]
P = [0] * 3
res = 100000000000

def dfs(l):
    global res
    if l >= N:
        if P[1] == 0 or P[2] == 0:
            return
        if P[0] == P[1] or P[1] == P[2] or P[0] == P[2]:
            return
        res = min(res, max(P) - min(P))
        return
    for i in range(3):
        P[i] += C[l]
        dfs(l+1)
        P[i] -= C[l]


dfs(0)
print(res)
