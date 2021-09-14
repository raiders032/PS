"""
https://www.acmicpc.net/problem/2075
2075.N번째 큰 수
골드5
풀이1.728ms
"""
import sys
import heapq

input = sys.stdin.readline
N = int(input())
board = list()
max_heap = []
num = 0
for _ in range(N):
    board.append(list(map(int, input().strip().split())))
for i in range(N):
    heapq.heappush(max_heap, (-board[N - 1][i], N - 1, i))
for _ in range(N):
    (num, x, y) = heapq.heappop(max_heap)
    heapq.heappush(max_heap, (-board[x - 1][y], x - 1, y))
print(-num)
