"""
https://www.acmicpc.net/problem/4948
4948.베르트랑 공준
실버2
풀이1.632ms
"""
from math import sqrt

N = 2 * 123457
is_prime = [True] * N

for i in range(2, int(sqrt(N))):
    if not is_prime[i]:
        continue
    for j in range(i * i, N, i):
        is_prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for j in range(n + 1, 2 * n + 1):
        if not is_prime[j]:
            continue
        count += 1
    print(count)
