"""
https://www.acmicpc.net/problem/3190
3190.뱀
골드4
풀이1.92ms
"""
import sys
import collections
input = sys.stdin.readline


def start_game():
    count = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    snake = collections.deque()
    snake.append((0, 0))
    visited[0][0] = True

    while True:
        snake_head = snake[-1]
        nx = snake_head[0] + dx[direction]
        ny = snake_head[1] + dy[direction]

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            break
        if visited[nx][ny]:
            break

        visited[nx][ny] = True
        snake.append((nx, ny))

        if not board[nx][ny]:
            snake_tail = snake.popleft()
            visited[snake_tail[0]][snake_tail[1]] = False
        else:
            board[nx][ny] = 0

        count += 1
        if commands and commands[0][0] == count:
            if commands[0][1] == 'L':
                direction = (direction + 3) % 4
            else:
                direction = (direction + 1) % 4
            commands.popleft()

    return count


N = int(input())
board = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

L = int(input())
commands = collections.deque()
for _ in range(L):
    second, command = input().split()
    commands.append((int(second), command))
print(start_game() + 1)