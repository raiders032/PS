"""
https://www.acmicpc.net/problem/13975
13975.파일 합치기 3
풀이1.5560ms
"""
import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    min_heap = []
    sheep_count = 0

    for file in list(map(int, input().split())):
       heapq.heappush(min_heap, file)

    while len(min_heap) != 1:
        file1 = heapq.heappop(min_heap)
        file2 = heapq.heappop(min_heap)
        heapq.heappush(min_heap, file1 + file2)
        sheep_count += file1 + file2

    print(sheep_count)