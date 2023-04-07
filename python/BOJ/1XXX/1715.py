"""
https://www.acmicpc.net/problem/1715
1715.카드 정렬하기
풀이2.224ms
"""
import sys
import heapq
input = sys.stdin.readline

N = int(input())
min_heap = []
for _ in range(N):
    heapq.heappush(min_heap, int(input()))

sheep_count = 0
while len(min_heap) != 1:
    min_card1 = heapq.heappop(min_heap)
    min_card2 = heapq.heappop(min_heap)
    sheep_count += min_card1 + min_card2
    heapq.heappush(min_heap, min_card1 + min_card2)
print(sheep_count)
