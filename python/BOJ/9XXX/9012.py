"""
https://www.acmicpc.net/problem/9012
9012.괄호
실버4
풀이2.76ms
"""
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    ps = input().rstrip()
    count = 0
    is_valid = True

    for index, parenthesis in enumerate(ps):
        if parenthesis == '(':
            count += 1
            continue

        if count == 0:
            is_valid = False
            break

        count -= 1

    if is_valid and count == 0:
        print("YES")
    else:
        print("NO")