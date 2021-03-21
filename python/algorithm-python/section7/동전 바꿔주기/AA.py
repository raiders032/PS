price = int(input())
num = int(input())
C = []
N = []
res = 0


def dfs(sum, l):
    global res
    if sum > price:
        return
    if sum == price:
        res += 1
        return
    for i in range(l, num):
        if N[i] > 0:
            N[i] -= 1
            dfs(sum + C[i], i)
            N[i] += 1


for _ in range(num):
    c, n = map(int, input().split())
    C.append(c)
    N.append(n)

dfs(0, 0)
print(res)
