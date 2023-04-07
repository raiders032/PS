"""
https://school.programmers.co.kr/learn/courses/30/lessons/92335
92335.k진수에서 소수 개수 구하기
풀이1
"""
import re
import math


def trans_to_k(n, k):
    if n < k:
        return str(n)
    return trans_to_k(n // k, k) + str(n % k)


def is_prime(number):
    if number == 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    result = trans_to_k(n, k)
    for number in re.split('[0]+', result):
        if not number.isdigit():
            continue
        if is_prime(int(number)):
            answer += 1

    return answer


print(solution(1000000, 3))