"""
https://www.acmicpc.net/problem/11286
11286.절댓값 힙
실버1
풀이2.296ms
"""
import sys
import heapq

input = sys.stdin.readline
min_heap = []
N = int(input())
for _ in range(N):
    num = int(input())

    if num != 0:
        heapq.heappush(min_heap, (abs(num), num))
        continue

    if min_heap:
        print(heapq.heappop(min_heap)[1])
    else:
        print(0)

