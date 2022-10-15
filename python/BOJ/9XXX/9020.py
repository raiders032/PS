"""
https://www.acmicpc.net/problem/9020
9020.골드바흐의 추측
풀이2.96ms
"""
import sys

input = sys.stdin.readline

is_prime = [True] * 10001
is_prime[0] = is_prime[1] = False
for i in range(2, 10001):
    if not is_prime[i]:
        continue

    for j in range(2 * i, 10001, i):
        is_prime[j] = False

for _ in range(int(input())):
    n = int(input())
    i = n // 2
    while True:
        if is_prime[i] and is_prime[n - i]:
            print(f'{i} {n - i}')
            break
        i -= 1






