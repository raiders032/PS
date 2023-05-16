"""
https://www.acmicpc.net/problem/17845
17845.수강 과목
풀이1.352ms(PyPy3)
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
weight = [0]
price = [0]
cache = [[0] * (n + 1) for _ in range(k + 1)]

for _ in range(k):
    p, w = map(int, input().split())
    weight.append(w)
    price.append(p)

for i in range(1, k + 1):
    for j in range(n + 1):
        cache[i][j] = cache[i - 1][j]
        if j - weight[i] >= 0:
            cache[i][j] = max(cache[i][j], cache[i - 1][j - weight[i]] + price[i])

print(cache[k][n])