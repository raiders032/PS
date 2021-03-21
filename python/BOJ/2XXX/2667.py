"""
2667.단지번호붙이기
실버1
DFS, BFS, 그래프이론, 그래프탐색
"""
import sys
from collections import deque


def get_cnt_by_bfs(x, y):
    cnt = 1
    q = deque()
    visited[x][y] = True
    q.append((x, y))
    while q:
        cur_x = q[0][0]
        cur_y = q[0][1]
        q.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue
            if visited[next_x][next_y] or board[next_x][next_y] == 0:
                continue
            visited[next_x][next_y] = True
            q.append((next_x, next_y))
            cnt += 1
    return cnt


input = sys.stdin.readline
N = int(input())
board = []
visited = [[False] * N for _ in range(N)]
cnts = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    row = list(map(int, input().rstrip()))
    board.append(row)
for r in range(N):
    for c in range(N):
        if visited[r][c] or board[r][c] == 0:
            continue
        cnts.append(get_cnt_by_bfs(r, c))
cnts.sort()
print(len(cnts))
for x in cnts:
    print(x)
