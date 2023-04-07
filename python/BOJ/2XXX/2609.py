""""
https://www.acmicpc.net/problem/2609
2609.최대공약수와 최소공배수
실버5
풀이2.
"""


def gcd(a, b):
    if a < b:
        a, b, = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())
gcd = gcd(a, b)
print(gcd)
print(a * b // gcd)
