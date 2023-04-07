"""
https://www.acmicpc.net/problem/2304
2304.창고 다각형
실버2
풀이2.72ms
"""
import sys

input = sys.stdin.readline
N = int(input())
pillars = [tuple(map(int, input().split())) for _ in range(N)]
pillars.sort()

max_height = 0
max_index = 0
for i in range(N):
    if max_height < pillars[i][1]:
        max_height = pillars[i][1]
        max_index = i

sheep_count = max_height
left = [pillars[0]]
for i in range(1, max_index + 1):
    if left[-1][1] <= pillars[i][1]:
        sheep_count += left[-1][1] * (pillars[i][0] - left[-1][0])
        left.append(pillars[i])

right = [pillars[N - 1]]
for i in range(N - 2, max_index - 1, -1):
    if right[-1][1] <= pillars[i][1]:
        sheep_count += right[-1][1] * (right[-1][0] - pillars[i][0])
        right.append(pillars[i])

print(sheep_count)