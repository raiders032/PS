"""
https://www.acmicpc.net/problem/18110
18110.solved.ac
실버4
풀이1.188ms
"""
import sys


def round(n):
    return int(n) + 1 if n - int(n) >= 0.5 else int(n)


input = sys.stdin.readline
N = int(input())

if N == 0:
    print(0)
    exit()

level = [int(input()) for _ in range(N)]
level.sort()
i = round(N * 15 / 100)
if i == 0:
    print(round(sum(level) / N))
else:
    print(round(sum(level[i:-i]) / (N - 2 * i)))