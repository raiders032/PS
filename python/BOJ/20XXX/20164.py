"""
https://www.acmicpc.net/problem/20164
20164.홀수 홀릭 호석
풀이1.48ms
"""
import sys

input = sys.stdin.readline

number = input().rstrip()
cache = dict()


def solve(number):
    if number in cache:
        return cache[number]

    odd_count = 0
    for digit in map(int, number):
        if digit % 2 == 1:
            odd_count += 1

    if len(number) == 1:
        cache[number] = [odd_count, odd_count]
        return cache[number]

    if len(number) == 2:
        (min_value, max_value) = solve(str(sum(map(int, number))))
        cache[number] = [odd_count + min_value, odd_count + max_value]
        return cache[number]

    cache[number] = [sys.maxsize, 0]
    for i in range(len(number) - 2):
        for j in range(i + 1, len(number) - 1):
            for k in range(j + 1, len(number)):
                sum_value = int(number[:j]) + int(number[j:k]) + int(number[k:])
                result = solve(str(sum_value))
                cache[number][0] = min(cache[number][0], result[0] + odd_count)
                cache[number][1] = max(cache[number][1], result[1] + odd_count)

    return cache[number]


answer = solve(number)
print(' '.join(map(str, answer)))
