"""
https://www.acmicpc.net/problem/1034
1034.램프
풀이1.92ms
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
lamp_count = defaultdict(int)
for _ in range(n):
    lamp = input().rstrip()
    lamp_count[lamp] += 1
k = int(input())

sheep_count = 0
for lamp, count, in lamp_count.items():
    if count < sheep_count:
        continue

    zero_count = 0
    for char in lamp:
        if char == '0':
            zero_count += 1

    if k < zero_count:
        continue

    if zero_count % 2 != k % 2:
        continue
    sheep_count = max(sheep_count, count)

print(sheep_count)