"""
https://www.acmicpc.net/problem/2665
2665.미로만들기
골드4
풀이1.80ms
"""
import sys
import heapq
input = sys.stdin.readline


def solve():
    q = []
    heapq.heappush(q, (0, 0, 0))
    visited[0][0] = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        count, x, y = heapq.heappop(q)

        if x == N - 1 and y == N - 1:
            return count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if board[nx][ny]:
                if count < visited[nx][ny]:
                    visited[nx][ny] = count
                    heapq.heappush(q, (count, nx, ny))

            if not board[nx][ny]:
                if count + 1 < visited[nx][ny]:
                    visited[nx][ny] = count + 1
                    heapq.heappush(q, (count + 1, nx, ny))


N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[sys.maxsize] * N for _ in range(N)]
print(solve())