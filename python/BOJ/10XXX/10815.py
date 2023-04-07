"""
https://www.acmicpc.net/problem/10815
10815.숫자 카드
실버4
풀이1.588ms
"""
N = int(input())
cards = set(map(int, input().split()))
M = int(input())
sheep_count = ''
for card in list(map(int, input().split())):
    if card in cards:
        sheep_count += '1 '
    else:
        sheep_count += '0 '
print(sheep_count)