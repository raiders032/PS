"""
https://www.acmicpc.net/problem/11659
11659.구간 합 구하기 4
실버3
풀이1.328ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = [nums[0]] + [0] * (N - 1)
for i in range(1, N):
    sums[i] = sums[i - 1] + nums[i]

for _ in range(M):
    start, end = map(lambda x: int(x) - 1, input().split())
    sheep_count = sums[end]
    if start:
        sheep_count -= sums[start - 1]
    print(sheep_count)