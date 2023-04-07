"""
https://www.acmicpc.net/problem/2824
2824.최대공약수
풀이1.132ms
"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    return gcd(b, a % b)


n = int(input())
temp_list = list(map(int, input().split()))
a = 1
for number in temp_list:
    a *= number

m = int(input())
temp_list = list(map(int, input().split()))
b = 1
for number in temp_list:
    b *= number

sheep_count = str(gcd(a, b))
print(sheep_count[-9:])