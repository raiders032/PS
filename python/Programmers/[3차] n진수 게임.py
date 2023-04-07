"""
https://school.programmers.co.kr/learn/courses/30/lessons/17687
[3차] n진수 게임
풀이1.100점
"""


def trans_to(number, n):
    number_to_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if number == 0:
        return '0'
    result = ''
    while number:
        result += number_to_hex[number % n]
        number = number // n
    return result[::-1]


def solution(n, t, m, p):
    answer = ''
    number = 0
    while len(answer) <= m * t:
        answer += trans_to(number, n)
        number += 1
    print(answer)
    return answer[p - 1::m][:t]


print(solution(2, 4, 2, 1))
# print(solution(16, 16, 2, 1))
# print(solution(16, 16, 2, 2))
# print(trans_to(0, 3))

"""
02468ACE111111111
02468ACE11111111

13579BDF012345678
13579BDF01234567
"""