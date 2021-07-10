"""
https://www.acmicpc.net/problem/11286
11286.절댓값 힙
실버1
풀이1.188ms
"""
import sys, heapq

input = sys.stdin.readline
min_heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap)[1])
        else:
            print(0)
        continue
    heapq.heappush(min_heap, (abs(x), x))