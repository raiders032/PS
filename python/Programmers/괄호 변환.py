"""
https://school.programmers.co.kr/learn/courses/30/lessons/60058
괄호 변환
풀이1
"""


def validate(u):
    stack = []
    for index in range(len(u)):
        if u[index] == '(':
            stack.append('(')
        else:
            if not stack or stack[-1] != '(':
                return False
            stack.pop()

    if stack:
        return False

    return True


def solution(p):
    if p == '':
        return ''
    u = ''
    v = ''
    l_count = 1 if p[0] == '(' else 0
    r_count = 1 if p[0] == ')' else 0

    for i in range(1, len(p)):
        if p[i] == '(':
            l_count += 1
        else:
            r_count += 1
        if l_count == r_count:
            u = p[:l_count + r_count]
            v = p[l_count + r_count:]
            break

    if validate(u):
        return u + solution(v)

    v = '(' + solution(v) + ')'
    u = u[1:-1]
    for char in u:
        if char == '(':
            v += ')'
        else:
            v += '('
    return v


print(solution("()))((()"))