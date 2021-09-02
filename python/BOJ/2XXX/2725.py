"""
https://www.acmicpc.net/problem/2725
2725.보이는 점의 개수
실버2
풀이1.992ms
"""
import sys


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


input = sys.stdin.readline
counts = [0] * 1001
counts[1] = 3

for x in range(2, 1001):
    counts[x] = counts[x - 1]
    for y in range(1, x):
        if get_gcd(x, y) == 1:
            counts[x] += 2

for _ in range(int(input())):
    N = int(input())
    print(counts[N])
