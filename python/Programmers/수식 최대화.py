from itertools import permutations


def make_post_expression(priority, expression):
    post_expression = []
    stack = []
    number = ''
    for char in expression:
        if char.isdigit():
            number += char
            continue

        post_expression.append(number)
        number = ''

        if not stack:
            stack.append(char)
            continue

        while stack and priority[stack[-1]] <= priority[char]:
            post_expression.append(stack.pop())
        stack.append(char)

    post_expression.append(number)

    while stack:
        post_expression.append(stack.pop())

    return post_expression


def eval_post_expression(expression):
    stack = []
    for e in expression:
        if e.isdigit():
            stack.append(e)
            continue
        operand1 = stack.pop()
        operand2 = stack.pop()
        stack.append(str(eval(operand2 + e + operand1)))

    return int(stack[-1])


def solution(expression):
    answer = 0
    operators = ['+', '-', '*']
    for op in permutations(operators):
        priority = dict()
        for i in range(3):
            priority[op[i]] = i
        post_expression = make_post_expression(priority, expression)
        answer = max(answer, abs(eval_post_expression(post_expression)))
    return answer


print(solution("100-200*300-500+20"))