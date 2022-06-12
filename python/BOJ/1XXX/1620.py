"""
https://www.acmicpc.net/problem/1620
1620.나는야 포켓몬 마스터 이다솜
실버4
풀이1.284ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
number_name = dict()
name_number = dict()

for i in range(N):
    name = input().rstrip()
    number_name[i + 1] = name
    name_number[name] = i + 1

for i in range(M):
    command = input().rstrip()
    if command.isdecimal():
        print(number_name[int(command)])
    else:
        print(name_number[command])
