"""
https://www.acmicpc.net/problem/2775
2775.부녀회장이 될테야
브론즈2
풀이1.80ms
"""
board = [[0] * 15 for _ in range(15)]
for i in range(15):
    board[0][i] = i
    board[i][1] = 1

for i in range(1, 15):
    for j in range(2, 15):
        board[i][j] = board[i - 1][j] + board[i][j - 1]

test_case = int(input())
for i in range(test_case):
    k = int(input())
    n = int(input())
    print(board[k][n])
