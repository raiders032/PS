"""
https://www.acmicpc.net/problem/1966
프린터 큐
실버3
풀이2.84ms
"""
import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    heap = []
    count = 0
    priorities = list(map(int, input().split()))

    for index, priority in enumerate(priorities):
        heapq.heappush(heap, (-priority, index, index))

    while True:
        priority, index, org_index = heapq.heappop(heap)
        count += 1

        if org_index == M:
            print(count)
            break

        while heap[0][1] < index:
            request = heapq.heappop(heap)
            heapq.heappush(heap, (request[0], request[1] + 100, request[2]))