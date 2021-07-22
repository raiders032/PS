"""
https://www.acmicpc.net/problem/10815
10815.숫자 카드
실버4
풀이1.588ms
"""
N = int(input())
cards = set(map(int, input().split()))
M = int(input())
answer = ''
for card in list(map(int, input().split())):
    if card in cards:
        answer += '1 '
    else:
        answer += '0 '
print(answer)