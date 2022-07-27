"""
https://www.acmicpc.net/problem/1456
1456.거의 소수
풀이1.5648ms
"""
import math
A, B = map(int, input().split())


def get_primes():
    is_prime = [True] * (int(math.sqrt(B)) + 1)
    is_prime[0], is_prime[1] = False, False
    result = 0
    current_number = 2

    while current_number ** 2 <= B:
        if not is_prime[current_number]:
            current_number += 1
            continue

        ex = 2
        while current_number ** ex <= B:
            if A <= current_number ** ex:
                result += 1
            ex += 1

        for j in range(current_number * current_number, int(math.sqrt(B)) + 1, current_number):
            is_prime[j] = False
        current_number += 1
    return result


print(get_primes())
