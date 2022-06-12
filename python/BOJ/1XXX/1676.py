"""
https://www.acmicpc.net/problem/1676
1676.팩토리얼 0의 개수
실버5
풀이1.68ms
"""


def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)


N = int(input())
fac = str(fac(N))
answer = 0

while fac[len(fac) - answer - 1] == '0':
    answer += 1

print(answer)