"""
https://www.acmicpc.net/problem/15596
15596.정수 N개의 합
브론즈2
구현
풀이1.152ms
"""


def solve(a: list) -> int:
    total = 0
    for num in a:
        total += num
    return total

