"""
https://programmers.co.kr/learn/courses/30/lessons/42586
기능개발
레벨2
스택
풀이1
"""


def solution(progresses, speeds):
    answer = []
    left_days = []
    for index in range(len(progresses)):
        left_day = (100 - progresses[index]) // speeds[index]
        if (100 - progresses[index]) % speeds[index] != 0:
            left_day += 1
        left_days.append(left_day)

    stack = []
    max_left_day = 0
    for left_day in left_days:
        if not stack:
            stack.append(left_day)
            max_left_day = left_day
        elif stack and max_left_day >= left_day:
            stack.append(left_day)
        else:
            answer.append(len(stack))
            stack = [left_day]
            max_left_day = left_day

    if stack:
        answer.append(len(stack))

    return answer


print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]	))