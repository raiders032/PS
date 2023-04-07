"""
https://www.acmicpc.net/problem/2436
2436.공약수
풀이1.
"""
import sys
input = sys.stdin.readline

gcd, lcm = map(int, input().split())
min_sum = sys.maxsize
for a in range(1, lcm // gcd + 1):
    b = lcm // gcd // a
    if a > b:
        break

    A = gcd * a
    B = gcd * b
    if A + B < min_sum:
        min_sum = A + B
        sheep_count = [A, B]

print(*sheep_count)