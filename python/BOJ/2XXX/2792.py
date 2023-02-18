"""
https://www.acmicpc.net/problem/2792
2792.보석상자
풀이1.532ms
"""
import math

n, m = map(int, input().split())
left = 0
jewels = []
right = 0

for _ in range(m):
    jewel = int(input())
    jewels.append(jewel)
    if right < jewel:
        right = jewel

while left + 1 < right:
    mid = (left + right) // 2
    count = 0

    for jewel in jewels:
        count += math.ceil(jewel / mid)

    if count <= n:
        right = mid
    else:
        left = mid

print(right)