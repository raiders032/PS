"""
https://www.acmicpc.net/problem/3687
3687.성냥개비
골드2
풀이1. 실패
"""
import sys


def solve_min(count, sum):
    global min_answer
    if count == n:
        min_answer = int(str(sum)[::-1])
        return True

    for cnt, number in min_digit.items():
        if count == 0 and number == 0:
            continue
        if count + cnt > n:
            continue
        if solve_min(count + cnt, sum * 10 + number):
            return True
    return False


def solve_max(count, sum):
    global max_answer
    if count == n:
        max_answer = int(str(sum)[::-1])
        return True

    for cnt, number in max_digit.items():
        if count == 0 and number == 0:
            continue
        if count + cnt > n:
            continue
        if solve_max(count + cnt, sum * 10 + number):
            return True
    return False


min_digit = {7: 8, 6: 0, 5: 2, 4: 4, 3: 7, 2: 1}
max_digit = {2: 1, 3: 7}
input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    n = int(input())
    max_answer, min_answer = 0, 0
    solve_max(0, 0)
    solve_min(0, 0)
    if n == 6:
        min_answer = 6
    print(min_answer, max_answer)
