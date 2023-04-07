"""
https://www.acmicpc.net/problem/2011
2011.암호코드
실버1
풀이2.96ms
"""
import sys
sys.setrecursionlimit(10 ** 6)


def decode(code):
    if code in cache:
        return cache[code]
    if code == '':
        return 1

    cache[code] = 0
    if 0 < int(code[-1:]):
        cache[code] += decode(code[:-1])
    if 10 <= int(code[-2:]) <= 26:
        cache[code] += decode(code[:-2])
    if cache[code] == 0:
        print(0)
        exit()
    cache[code] %= 1000000
    return cache[code]


code = input()
cache = dict()
print(decode(code))