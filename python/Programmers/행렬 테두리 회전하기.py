"""
https://school.programmers.co.kr/learn/courses/30/lessons/77485
행렬 테두리 회전하기
풀이1.100점
"""


def solution(rows, columns, queries):
    answer = []

    board = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = columns * i + j + 1

    for query in queries:
        x1, y1, x2, y2 = map(lambda n: n - 1, query)
        temp = board[x1][y1]
        min_number = temp

        for x in range(x1, x2):
            board[x][y1] = board[x + 1][y1]
            min_number = min(min_number, board[x][y1])

        for y in range(y1, y2):
            board[x2][y] = board[x2][y + 1]
            min_number = min(min_number, board[x2][y])

        for x in range(x2, x1, -1):
            board[x][y2] = board[x - 1][y2]
            min_number = min(min_number, board[x][y2])

        for y in range(y2, y1, -1):
            board[x1][y] = board[x1][y - 1]
            min_number = min(min_number, board[x1][y])

        board[x1][y1 + 1] = temp
        answer.append(min_number)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
