"""
https://www.acmicpc.net/problem/3055
3055.탈출
골드4
풀이1.92ms
"""
import sys
import collections
input = sys.stdin.readline


def get_min_distance():
    q = collections.deque()
    for x, y in start_water:
        q.append(('*', x, y))
        water_visited[x][y] = True
    q.append(('S', start_x, start_y))
    hedgehog_visited[start_x][start_y] = 1

    while q:
        t, x, y = q.popleft()

        if board[x][y] == 'D':
            return hedgehog_visited[x][y] - 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            if board[nx][ny] == 'X':
                continue

            if t == 'S':
                if hedgehog_visited[nx][ny] or water_visited[nx][ny]:
                    continue
                hedgehog_visited[nx][ny] = hedgehog_visited[x][y] + 1
                q.append(('S', nx, ny))

            elif t == '*':
                if water_visited[nx][ny] or board[nx][ny] == 'D':
                    continue
                water_visited[nx][ny] = True
                q.append(('*', nx, ny))

    return 0


R, C = map(int, input().split())
water_visited = [[False] * C for _ in range(R)]
hedgehog_visited = [[0] * C for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
board = [[0] * C for _ in range(R)]
start_water = []

for i in range(R):
    for j, char in enumerate(input().rstrip()):
        board[i][j] = char
        if char == 'S':
            start_x = i
            start_y = j
        if char == '*':
            start_water.append((i, j))

result = get_min_distance()
print(result if result else 'KAKTUS')
