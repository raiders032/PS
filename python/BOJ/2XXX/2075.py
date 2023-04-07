"""
https://www.acmicpc.net/problem/2075
2075.N번째 큰 수
골드5
풀이2.
"""
import sys
import heapq

input = sys.stdin.readline
N = int(input())
min_heap = list(map(int, input().split()))
heapq.heapify(min_heap)
print(f'min:{min_heap[0]}')
for i in range(N - 1):
    for num in map(int, input().split()):
        if min_heap[0] < num:
            heapq.heappush(min_heap, num)
            heapq.heappop(min_heap)
    print(f'min:{min_heap[0]}')

print(min_heap[0])