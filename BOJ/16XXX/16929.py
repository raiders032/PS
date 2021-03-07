'''
https://www.acmicpc.net/problem/16929
16929번 Two Dots
골드4
깊이우선탐색,그래프이론,그래프탐색
풀이1. 실패
'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def dfs(sx, sy, x, y, dist):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if sx == nx and sy == ny and dist > 1:
            print("Yes")
            exit(0)
        if board[x][y] == board[nx][ny] and visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(sx, sy, nx, ny, dist + 1)
            visited[nx][ny] = False


for x in range(N):
    for y in range(M):
        cnt = 0
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[x][y] == board[nx][ny]:
                cnt += 1
        if cnt < 2:
            continue
        visited[x][y] = True
        dfs(x, y, x, y, 0)
        visited[x][y] = False
print("No")
