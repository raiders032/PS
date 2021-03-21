"""
https://www.acmicpc.net/problem/1918
1918.후위 표기식
골드4
자료구조,스택
풀이1.72ms
"""


def push_operators(operator):
    global post_exp
    if operator == ')':
        while operators_stack[-1] != '(':
            post_exp += operators_stack.pop()
        operators_stack.pop()

    elif operator == '*' or operator == '/':
        while operators_stack and (operators_stack[-1] == '*' or operators_stack[-1] == '/'):
            post_exp += operators_stack.pop()
        operators_stack.append(operator)

    elif operator == '+' or operator == '-':
        while operators_stack and operators_stack[-1] != '(':
            post_exp += operators_stack.pop()
        operators_stack.append(operator)

    elif operator == '(':
        operators_stack.append(operator)


exp = input()
post_exp = ""
operators_stack = []

for char in exp:
    if char.isalpha():
        post_exp += char
        continue
    push_operators(char)

for _ in range(len(operators_stack)):
    post_exp += operators_stack.pop()

print(post_exp)

