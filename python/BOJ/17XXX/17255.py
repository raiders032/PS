"""
https://www.acmicpc.net/problem/17255
17255.N으로 만들기
풀이1.96ms
"""
from collections import defaultdict


def get_count(number):
    if cache[number]:
        return cache[number]
    if len(number) == 1:
        return 1

    left_number = number[:len(number) - 1]
    cache[number] += get_count(left_number)

    right_number = number[1:]
    cache[number] += get_count(right_number) if left_number != right_number else 0

    return cache[number]


cache = defaultdict(int)
print(get_count((input())))
