"""
https://www.acmicpc.net/problem/2581
2581.소수
실버5
수학
풀이1.72ms
"""
from math import sqrt

M = int(input())
N = int(input())
is_prime = [False] * 2 + [True] * (N - 1)

for i in range(2, int(sqrt(N)) + 1):
    if not is_prime[i]:
        continue
    for j in range(i * i, N + 1, i):
        is_prime[j] = False

total = 0
min_prime = 0

for i in range(M, N + 1):
    if not is_prime[i]:
        continue
    if min_prime == 0:
        min_prime = i
    total += i

if total == 0:
    print(-1)
else:
    print(total)
    print(min_prime)

