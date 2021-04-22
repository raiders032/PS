"""
https://programmers.co.kr/learn/courses/30/lessons/42883
큰 수 만들기
탐욕법
풀이2
"""


def solution(number, k):
    count = 0
    length = len(number)
    index = 0

    while count < k:
        for i in range(index, length - 1):
            if int(number[i]) >= int(number[i + 1]):
                continue
            else:
                count += 1
                index = i - 1 if i - 1 >= 0 else 0
                number = number[0:i] + number[i + 1: length]
                length -= 1
                break
        else:
            number = number[0: -(k - count)]
            break

    return number


print(solution("123456", 1))
