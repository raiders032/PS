"""
https://www.acmicpc.net/problem/2581
2581.소수
실버5
수학
풀이2
"""
from math import sqrt
import sys

N = int(input())
M = int(input())
is_prime = [True] * (M + 1)

for i in range(2, int(sqrt(M + 1)) + 1):
    if not is_prime[i]:
        continue

    for j in range(2 * i, M + 1, i):
        is_prime[j] = False

sum = 0
min_prime = 987654321
for i in range(N, M + 1):
    if is_prime[i]:
        sum += i
        min_prime = min(min_prime, i)

if min_prime != 987654321:
    print(sum)
    print(min_prime)
else:
    print(-1)