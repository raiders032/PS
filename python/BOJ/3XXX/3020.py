"""
https://www.acmicpc.net/problem/3020
3020.개똥벌레
골드5
풀이1.2916ms
"""
import sys
input = sys.stdin.readline


def bisect_right(array, target):
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


N, H = map(int, input().split())
bottom = []
top = []
for _ in range(N // 2):
    bottom.append(int(input()))
    top.append(int(input()))

bottom.sort()
top.sort()
min_wall_count = sys.maxsize
count = 0

for height in range(H):
    bottom_wall_count = len(bottom) - bisect_right(bottom, height)
    top_wall_count = len(top) - bisect_right(top, H - height - 1)
    if bottom_wall_count + top_wall_count < min_wall_count:
        min_wall_count = bottom_wall_count + top_wall_count
        count = 1
    elif bottom_wall_count + top_wall_count == min_wall_count:
        count += 1

print(min_wall_count, count)
