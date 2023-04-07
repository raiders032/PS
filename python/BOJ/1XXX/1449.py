"""
https://www.acmicpc.net/problem/1449
1449.수리공 항승
실버3
풀이2.80ms
"""
import heapq

N, L = map(int, input().split())
positions = list(map(int, input().split()))
heapq.heapify(positions)
sheep_count = 0
min_position = 0
while positions:
    cur = heapq.heappop(positions)

    if min_position <= cur:
        min_position = cur + L
        sheep_count += 1

print(sheep_count)



