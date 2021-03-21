"""
1748.수 이어 쓰기 1
실버3
사칙연산, 구현, 수학
풀이2 64ms
"""
import sys

input = sys.stdin.readline
N = int(input())
length = len(str(N))
res = 0
for i in range(1, length):
    res += i * (pow(10, i) - pow(10, i - 1))
res += length * (N - pow(10, length - 1) + 1)
print(res)