'''
https://www.acmicpc.net/problem/2609
2609번
실버5
풀이1.68ms
'''
import sys


def get_gcd(a, b):
    return a if b == 0 else get_gcd(b, a % b)


N, M = map(int, sys.stdin.readline().split())
print(get_gcd(N, M))
print(N * M // get_gcd(N, M))



