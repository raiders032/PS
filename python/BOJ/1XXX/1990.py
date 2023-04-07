"""
https://www.acmicpc.net/problem/1990
1990.소수인팰린드롬
풀이1.3380ms
"""
import sys
import math

input = sys.stdin.readline


def is_palindrome(word: str):
    return word == word[::-1]


def is_prime(number: int):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


a, b = map(int, input().split())
answer = []
for i in range(a, 10000001 if b > 10000000 else b + 1):
    if is_palindrome(str(i)) and is_prime(i):
        answer.append(str(i))
answer.append("-1")

print("\n".join(answer))
