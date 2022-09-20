"""
https://school.programmers.co.kr/learn/courses/30/lessons/92344
파괴되지 않은 건물
풀이1.100점
"""
from collections import defaultdict


def solution(board, skills):
    answer = 0
    position_degree = defaultdict(int)
    n = len(board)
    m = len(board[0])
    d = [[0] * (m + 1) for _ in range(n + 1)]

    for skill in skills:
        if skill[0] == 1:
            position_degree[tuple(skill[1:5])] -= skill[5]
        else:
            position_degree[tuple(skill[1:5])] += skill[5]

    for position, degree in position_degree.items():
        if degree == 0:
            continue
        r1, c1, r2, c2 = position
        d[r1][c1] += degree
        d[r1][c2 + 1] -= degree
        d[r2 + 1][c1] -= degree
        d[r2 + 1][c2 + 1] += degree

    for r in range(1, n):
        for c in range(m):
            d[r][c] += d[r - 1][c]

    for r in range(n):
        for c in range(1, m):
            d[r][c] += d[r][c - 1]

    for r in range(n):
        for c in range(m):
            if d[r][c] + board[r][c] > 0:
                answer += 1

    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
