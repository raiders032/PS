"""
https://programmers.co.kr/learn/courses/30/lessons/42883
큰 수 만들기
탐욕법
풀이1.시간초과
"""


def solution(number, k):
    count = 0

    while count < k:
        for index in range(len(number) - 1):
            if int(number[index]) >= int(number[index + 1]):
                continue
            else:
                count += 1
                number = number[0:index] + number[index + 1: len(number)]
                break
        else:
            number = number[0: -(k - count)]
            break
    return str(number)


print(solution("321", 1))
