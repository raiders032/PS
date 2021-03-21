"""
6064.카잉 달력
실버1
중국인의나머지정리, 수학, 정수론
풀이2 312ms(pypy3)
"""
import sys

input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    M, N, x, y = map(int, input().rstrip().split())
    x -= 1
    y -= 1
    year = x
    while year < M * N:
        if year % N == y:
            print(year + 1)
            break
        year += M
    else:
        print(-1)