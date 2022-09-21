"""
https://www.acmicpc.net/problem/17124
17124.두 개의 배열
풀이2.816ms(PyPy3)
"""
import sys
input = sys.stdin.readline


def find(number):
    if number < B[0]:
        return B[0]
    elif B[-1] < number:
        return B[-1]

    left = 0
    right = len(B) - 1
    while left <= right:
        mid = (left + right) // 2

        if B[mid] < number:
            left = mid + 1
        elif number < B[mid]:
            right = mid - 1
        else:
            return B[mid]

    if number < B[mid]:
        return B[mid] if B[mid] - number < number - B[mid - 1] else B[mid - 1]
    else:
        return B[mid] if number - B[mid] <= B[mid + 1] - number else B[mid + 1]


for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    answer = 0
    for number in A:
        answer += find(number)
    print(answer)