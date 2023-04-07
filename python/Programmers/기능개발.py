"""
https://programmers.co.kr/learn/courses/30/lessons/42586
기능개발
레벨2
스택
풀이2
"""


def solution(progresses, speeds):
    answer = []
    left_days = []

    for index, progress in enumerate(progresses):
        if (100 - progress) % speeds[index] == 0:
            left_days.append((100 - progress) // speeds[index])
        else:
            left_days.append((100 - progress) // speeds[index] + 1)

    count = 1
    max_left_day = left_days[0]

    for i in range(1, len(progresses)):
        if max_left_day < left_days[i]:
            max_left_day = left_days[i]
            answer.append(count)
            count = 1
        else:
            count += 1
    answer.append(count)

    return answer
