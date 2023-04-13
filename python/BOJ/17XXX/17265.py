"""
https://www.acmicpc.net/problem/17265
17265.나의 인생에는 수학과 함께
풀이1.44ms
"""
import sys

input = sys.stdin.readline


def get_all_expressions(x, y, result):
    if x == n - 1 and y == n - 1:
        answer[0] = max(answer[0], result)
        answer[1] = min(answer[1], result)
        return

    for dir in range(2):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx >= n or ny >= n or visited[nx][ny]:
            continue

        visited[nx][ny] = True
        if not board[x][y].isdigit():
            get_all_expressions(nx, ny, eval(''.join([str(result), board[x][y], board[nx][ny]])))
        else:
            get_all_expressions(nx, ny, result)
        visited[nx][ny] = False


n = int(input())
board = [list(input().rstrip().split()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = [-sys.maxsize, sys.maxsize]
dx = [1, 0]
dy = [0, 1]
visited[0][0] = True
get_all_expressions(0, 0, int(board[0][0]))
print(' '.join(map(str, answer)))
