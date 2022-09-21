"""
https://school.programmers.co.kr/learn/courses/30/lessons/60061
기둥과 보 설치
풀이1.100점
"""


def solution(n, build_frame):
    columns = set()
    girders = set()

    def check_column(x, y):
        return y == 0 or (x, y - 1) in columns or (x - 1, y) in girders or (x, y) in girders

    def check_girder(x, y):
        return (x, y - 1) in columns or (x + 1, y - 1) in columns or ((x - 1, y) in girders and (x + 1, y) in girders)

    def is_valid():
        for x, y in columns:
            if not check_column(x, y):
                return False
        for x, y in girders:
            if not check_girder(x, y):
                return False
        return True

    for x, y, a, b in build_frame:
        if b == 0:
            if a == 0:
                columns.remove((x, y))
                if not is_valid():
                    columns.add((x, y))
            else:
                girders.remove((x, y))
                if not is_valid():
                    girders.add((x, y))
        else:
            if a == 0:
                if check_column(x, y):
                    columns.add((x, y))
            else:
                if check_girder(x, y):
                    girders.add((x, y))

    answer = list(map(lambda x: [x[0], x[1], 0], columns))
    answer += list(map(lambda x: [x[0], x[1], 1], girders))
    return sorted(answer)


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))

print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
