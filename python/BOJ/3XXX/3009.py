"""
https://www.acmicpc.net/problem/3009
3009.네 번째 점
브론즈3
풀이1.
"""
from collections import defaultdict

X = defaultdict(int)
Y = defaultdict(int)

for i in range(3):
    x, y = map(int, input().split())
    X[x] += 1
    Y[y] += 1

for k, v in X.items():
    if v == 1:
        print(k, end=' ')

for k, v in Y.items():
    if v == 1:
        print(k)