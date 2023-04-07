"""
https://www.acmicpc.net/problem/2667
2667.단지번호붙이기
실버1
풀이2.68ms
"""
import sys
sys.setrecursionlimit(10 ** 6)


def get_area(x, y):
    visited[x][y] = True
    area = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if visited[nx][ny] or not board[nx][ny]:
            continue

        area += get_area(nx, ny)

    return area


N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]
# print(original_board)
visited = [[False] * N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

counts = []
for i in range(N):
    for j in range(N):
        if visited[i][j] or not board[i][j]:
            continue
        counts.append(get_area(i, j))

print(len(counts))
counts.sort()
for count in counts:
    print(count)