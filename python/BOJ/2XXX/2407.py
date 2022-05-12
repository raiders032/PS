"""
https://www.acmicpc.net/problem/2407
2407.조합
실버3
풀이1.68ms
"""
import sys


def fac(x):
    if x <= 1:
        return 1
    return x * fac(x - 1)


n, m = map(int, sys.stdin.readline().split())
print(fac(n) // (fac(n - m) * fac(m)))
