"""
https://www.acmicpc.net/problem/14888
14888.연산자 끼워넣기
실버1
백트래킹,브루트포스
풀이1.128ms
"""
import sys


def solve(level, result):
    global ans_min, ans_max
    if level == N:
        ans_min = min(ans_min, result)
        ans_max = max(ans_max, result)
        return

    for op_num in range(4):
        if not operators[op_num]:
            continue
        operators[op_num] -= 1
        solve(level + 1, operate(op_num, result, operands[level]))
        operators[op_num] += 1


def operate(operator_num, num1, num2):
    if operator_num == 0:
        return num1 + num2
    elif operator_num == 1:
        return num1 - num2
    elif operator_num == 2:
        return num1 * num2
    elif operator_num == 3:
        if num1 < 0:
            return -(-num1 // num2)
        return num1 // num2


ans_min = sys.maxsize
ans_max = -sys.maxsize
input = sys.stdin.readline
N = int(input())
operands = list(map(int, input().split()))
operators = list(map(int, input().split()))
solve(1, operands[0])
print(ans_max)
print(ans_min)