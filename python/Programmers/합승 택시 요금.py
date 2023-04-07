"""
https://school.programmers.co.kr/learn/courses/30/lessons/72413
합승 택시 요금
풀이1.100점
"""
import sys


def solution(n, s, a, b, fares):
    min_fare = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        min_fare[i][i] = 0

    for v1, v2, w in fares:
        min_fare[v1][v2] = min(min_fare[v1][v2], w)
        min_fare[v2][v1] = min(min_fare[v2][v1], w)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if min_fare[j][i] + min_fare[i][k] < min_fare[j][k]:
                    min_fare[j][k] = min_fare[j][i] + min_fare[i][k]

    answer = sys.maxsize
    for i in range(1, n + 1):
        answer = min(answer, min_fare[s][i] + min_fare[i][a] + min_fare[i][b])
    return answer


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
