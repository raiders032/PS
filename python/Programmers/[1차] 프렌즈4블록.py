"""
https://school.programmers.co.kr/learn/courses/30/lessons/17679
[1차] 프렌즈4블록
풀이1.100
"""
from collections import deque


def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])

    while True:
        check = [[False] * n for _ in range(m)]

        game_over = True
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == 'X':
                    continue
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    game_over = False
                    check[i][j] = True
                    check[i + 1][j] = True
                    check[i][j + 1] = True
                    check[i + 1][j + 1] = True

        if game_over:
            break

        columns = [deque() for _ in range(n)]
        for y in range(n):
            for x in range(m - 1, -1, -1):
                if check[x][y]:
                    answer += 1
                    continue
                columns[y].append(board[x][y])

        board = [['X'] * n for _ in range(m)]
        for y in range(n):
            for i in range(len(columns[y])):
                board[m - i - 1][y] = columns[y].popleft()

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
