"""
https://www.acmicpc.net/problem/2168
2168.타일 위의 대각선
실버1
풀이1.68ms
"""


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


x, y = map(int, input().split())
print(x + y - gcd(x, y))