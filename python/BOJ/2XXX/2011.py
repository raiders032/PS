"""
https://www.acmicpc.net/problem/2011
2011.암호코드
실버1
풀이1.120ms
"""
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)


def solve(string):
    if string in cache:
        return cache[string]

    if not string:
        return 1

    number = int(string[-1])

    if 1 <= number <= 9:
        cache[string] += solve(string[:-1])
        cache[string] %= 1000000

    if len(string) <= 1:
        return cache[string]

    number = int(string[-2:])

    if 10 <= number <= 26:
        cache[string] += solve(string[:-2])
        cache[string] %= 1000000

    return cache[string]


string = input()
cache = defaultdict(int)
print(solve(string))
