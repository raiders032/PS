"""
https://www.acmicpc.net/problem/9020
9020.골드바흐의 추측
실버1
풀이1.532ms
"""
from math import sqrt

is_prime = [True] * 10001

for i in range(2, int(sqrt(10000))):
    if not is_prime[i]:
        continue
    for j in range(i * i, 10001, i):
        is_prime[j] = False

test_case = int(input())

for i in range(test_case):
    n = int(input())
    mid = n // 2

    for num in range(mid, 10001):
        if not is_prime[num]:
            continue
        if not is_prime[n - num]:
            continue
        print(f'{n - num} {num}')
        break





