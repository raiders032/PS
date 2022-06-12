"""
https://www.acmicpc.net/problem/11723
11723.집합
실버5
풀이1.4564ms
"""
import sys

input = sys.stdin.readline
M = int(input())
container = set()

for _ in range(M):
    command = input()

    if command.startswith('all'):
        container = {i for i in range(1, 21)}
        continue

    if command.startswith("empty"):
        container.clear()
        continue

    command, number = command.split()
    number = int(number)

    if command == 'add':
        container.add(number)

    elif command == 'remove':
        container.discard(number)

    elif command == 'toggle':
        if number in container:
            container.discard(number)
        else:
            container.add(number)
    else:
        print(int(number in container))