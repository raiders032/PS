"""
https://programmers.co.kr/learn/courses/30/lessons/42840
모의고사
레벨1
풀이2
"""


def solution(array):
    answers = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    result = []
    max_count = 0

    for i in range(3):
        count = 0
        for index, answer in enumerate(array):
            if answers[i][index % len(answers[i])] == answer:
                count += 1

        if max_count <= count:
            if max_count == count:
                result.append(i + 1)
            else:
                result = [i + 1]
            max_count = count

    return result
