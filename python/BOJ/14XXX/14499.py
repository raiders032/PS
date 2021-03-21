"""
14499. 주사위 굴리기
골드5
구현, 시뮬레이션
풀이1 68ms
"""
import sys


def roll_dice(dir):
    if dir == 1:
        dice[1][1], dice[1][2] = dice[1][2], dice[1][1]
        dice[1][0], dice[1][1] = dice[1][1], dice[1][0]
        dice[1][0], dice[3][1] = dice[3][1], dice[1][0]
    elif dir == 2:
        dice[1][0], dice[1][1] = dice[1][1], dice[1][0]
        dice[1][1], dice[1][2] = dice[1][2], dice[1][1]
        dice[1][2], dice[3][1] = dice[3][1], dice[1][2]
    elif dir == 3:
        dice[0][1], dice[1][1] = dice[1][1], dice[0][1]
        dice[1][1], dice[2][1] = dice[2][1], dice[1][1]
        dice[2][1], dice[3][1] = dice[3][1], dice[2][1]
    else:
        dice[2][1], dice[3][1] = dice[3][1], dice[2][1]
        dice[1][1], dice[2][1] = dice[2][1], dice[1][1]
        dice[0][1], dice[1][1] = dice[1][1], dice[0][1]


input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [[0 for _ in range(3)] for _ in range(4)]

for dir in map(int, input().split()):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    roll_dice(dir)
    print(dice[1][1])
    if board[nx][ny] == 0:
        board[nx][ny] = dice[3][1]
    else:
        dice[3][1] = board[nx][ny]
        board[nx][ny] = 0
    x = nx
    y = ny
