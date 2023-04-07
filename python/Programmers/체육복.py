"""
https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3#
체육복
레벨1
풀이2
"""


def solution(n, lost, reserve):
    answer = 0
    counts = [0] + [1] * n + [0]

    for index in lost:
        counts[index] -= 1

    for index in reserve:
        counts[index] += 1

    for i in range(1, n + 1):
        if counts[i]:
            answer += 1
            continue

        if counts[i - 1] > 1:
            answer += 1

        elif counts[i + 1] > 1:
            counts[i + 1] -= 1
            answer += 1

    return answer
