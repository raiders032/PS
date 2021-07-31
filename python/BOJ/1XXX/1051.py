"""
https://www.acmicpc.net/problem/1051
1051.숫자 정사각형
실버3
풀이1.104ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
ans = 1

for i in range(N - 1):
    for j in range(M - 1):
        k = 1
        while i + k < N and j + k < M:
            if board[i][j] == board[i + k][j] and board[i][j] == board[i][j + k] and board[i][j] == board[i + k][j + k]:
                ans = max(ans, (k + 1) ** 2)
            k += 1
print(ans)

"""
4 4
1234
1234
1255
1255 
1
---
5 10
9999999999
9999999999
9999999999
9999999999
9999999999
25
---
2 2
12
21
1
---

"""