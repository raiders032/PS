import sys

"""
https://www.acmicpc.net/problem/10814
10814.나이순 정렬
실버5
풀이1.292ms
"""

input = sys.stdin.readline
n = int(input())
persons = []

for _ in range(n):
    age, name = input().split()
    persons.append((int(age), name))

persons.sort(key=lambda x: x[0])

for age, name in persons:
    print(age, name)
