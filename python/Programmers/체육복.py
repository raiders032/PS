"""
https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3#
체육복
레벨1
탐욕
풀이1
"""


def solution(n, lost, reserve):
    answer = 0
    clothes = [1] * n

    for index in lost:
        clothes[index - 1] -= 1

    for index in reserve:
        clothes[index - 1] += 1

    for index in range(n):
        if clothes[index]:
            answer += 1
            continue

        if index and clothes[index - 1] == 2:
            clothes[index - 1] = 1
            clothes[index] = 1
            answer += 1

        elif index < n - 1 and clothes[index + 1] == 2:
            clothes[index + 1] = 1
            clothes[index] = 1
            answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))