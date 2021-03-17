"""
https://www.acmicpc.net/problem/16928
16928.뱀과 사다리 게임
실버2
BFS
풀이2.96ms
"""
import sys
from collections import deque


def solve():
    q = deque([0])
    visited = [[0] * 10 for _ in range(10)]
    visited[0][0] = 1

    while q:
        current_position = q.popleft()
        current_position_x = current_position // 10
        current_position_y = current_position % 10
        if current_position == 99:
            return visited[9][9] - 1

        for dice_num in range(1, 7):
            next_position = current_position + dice_num

            if next_position >= 100 or visited[next_position // 10][next_position % 10]:
                continue

            visited[next_position // 10][next_position % 10] = visited[current_position_x][current_position_y] + 1

            if board[next_position // 10][next_position % 10]:
                next_position = board[next_position // 10][next_position % 10]
                if visited[next_position // 10][next_position % 10]:
                    continue
                visited[next_position // 10][next_position % 10] = visited[current_position_x][current_position_y] + 1

            q.append(next_position)
    return -1


input = sys.stdin.readline
N, M = map(int, input().split())
board = [[0] * 10 for _ in range(10)]

for i in range(N + M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x // 10][x % 10] = y

print(solve())
