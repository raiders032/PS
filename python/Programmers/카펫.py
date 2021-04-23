"""
https://programmers.co.kr/learn/courses/30/lessons/42842
카펫
레벨2
완점탐색
풀이1
"""


def solution(brown, yellow):
    answer = []
    row, col = 3, 3
    cell_count = brown + yellow
    while True:
        if cell_count % row != 0:
            row += 1
            continue
        col = cell_count // row
        if row <= col and 2 * row + 2 * col - 4 == brown:
            return [col, row]
        row += 1
    return answer


print(solution(24, 24))