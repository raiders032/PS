"""
https://www.acmicpc.net/problem/1455
1455.뒤집기 II
풀이1.96ms
"""
import sys
input = sys.stdin.readline


def toggle(x, y):
    global answer
    answer += 1
    for i in range(x + 1):
        for j in range(y + 1):
            coins[i][j] = 1 if coins[i][j] == 0 else 0


n, m = map(int, input().split())
coins = [list(map(int, input().rstrip())) for _ in range(n)]
answer = 0

x = n - 1
y = m - 1

while x >= 0 and y >= 0:
    if coins[x][y] == 1:
        toggle(x, y)

    for j in range(m - 2, -1, -1):
        if coins[x][j] == 1:
            toggle(x, j)

    for i in range(n - 2, -1, -1):
        if coins[i][y] == 1:
            toggle(i, y)

    x -= 1
    y -= 1

print(answer)