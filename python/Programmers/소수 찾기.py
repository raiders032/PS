"""
https://programmers.co.kr/learn/courses/30/lessons/42839
소수 찾기
완전탐색
풀이1
"""
from math import sqrt

is_prime = [False, False] + [True] * 9999998
visited = []
primes = set()
nums = []


def dfs(limit, level, number):
    global visited, primes
    if is_prime[number]:
        primes.add(number)

    if level == limit:
        return

    for i in range(limit):
        if visited[i]:
            continue
        visited[i] = True
        dfs(limit, level + 1, number * 10 + nums[i])
        visited[i] = False


def eratosthenes_sieve():
    for number in range(2, int(sqrt(10000000)) + 1):
        if not is_prime[number]:
            continue
        for next_num in range(2 * number, 10000000, number):
            is_prime[next_num] = False


def solution(numbers):
    global visited, nums
    nums = list(map(int, numbers))
    eratosthenes_sieve()
    visited = [False] * len(numbers)
    dfs(len(numbers), 0, 0)
    return len(primes)


print(solution("011"))