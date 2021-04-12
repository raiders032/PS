"""
https://programmers.co.kr/learn/courses/30/lessons/12901#
2016년
풀이1
"""


def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    num = -1

    for i in range(a - 1):
        num += months[i]

    num += b

    return days[num % 7]


print(solution(5, 24))