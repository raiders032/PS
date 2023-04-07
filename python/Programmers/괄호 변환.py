"""
https://school.programmers.co.kr/learn/courses/30/lessons/60058
괄호 변환
풀이2
"""

import sys

sys.setrecursionlimit(10 ** 6)


def is_valid(parenthesis):
    open_count = 0
    for i in range(len(parenthesis)):
        if parenthesis[i] == '(':
            open_count += 1
        else:
            if not open_count:
                return False
            open_count -= 1
    return True


def solution(p):
    if not p:
        return ''
    if is_valid(p):
        return p

    open_count = 0
    close_count = 0
    for i in range(len(p)):
        if open_count and open_count == close_count:
            break
        if p[i] == '(':
            open_count += 1
        else:
            close_count += 1

    u = p[:i]
    v = p[i:]
    print(f'p:{p}, open_count:{open_count}, close_count:{close_count}')
    print(f'u:{u}, v:{v}')

    if is_valid(u):
        return u + solution(v)

    answer = '('
    answer += solution(v)
    answer += ')'
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('

    return answer


print(solution("(()())()"))