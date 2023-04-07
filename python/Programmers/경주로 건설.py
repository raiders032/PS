"""
https://school.programmers.co.kr/learn/courses/30/lessons/67259
경주로 건설
풀이1.100점
"""
from collections import deque
import sys


def solution(board):
    def visit(x, y, p, d):
        visited = [[sys.maxsize] * n for _ in range(n)]
        queue = deque()
        visited[0][0] = 0
        queue.append((x, y, p, d))

        while queue:
            x, y, price, direction = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if board[nx][ny]:
                    continue

                next_price = price + 100 if direction == i else price + 600
                if visited[nx][ny] <= next_price:
                    continue

                visited[nx][ny] = next_price
                queue.append((nx, ny, next_price, i))

        return visited[n - 1][n - 1]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(board)

    return min(visit(0, 0, 0, 1), visit(0, 0, 0, 2))


print(solution([[0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
