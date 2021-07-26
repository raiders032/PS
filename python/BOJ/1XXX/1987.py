"""
https://www.acmicpc.net/problem/1987
1987.알파벳
골드4
풀이1.5372ms
"""
import sys


def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    visited[ord(board[x][y]) - ord('A')] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if visited[ord(board[nx][ny]) - ord('A')]:
            continue
        visited[ord(board[nx][ny]) - ord('A')] = True
        dfs(nx, ny, count + 1)
        visited[ord(board[nx][ny]) - ord('A')] = False


input = sys.stdin.readline
R, C = map(int, input().split())
board = [input() for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [False] * 26
ans = 0
dfs(0, 0, 1)
print(ans)
