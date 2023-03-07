"""
https://www.acmicpc.net/problem/1202
1202.보석 도둑
풀이1.1468ms
"""
import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort()
bags.sort()
available_gem = []
answer = 0

for bag in bags:
    while gems and gems[0][0] <= bag:
        min_weight_gem = heapq.heappop(gems)
        heapq.heappush(available_gem, -min_weight_gem[1])

    if available_gem:
        max_gem_price = -heapq.heappop(available_gem)
        answer += max_gem_price

print(answer)