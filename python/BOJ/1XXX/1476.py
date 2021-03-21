'''
1476번 날짜 계산 실버5
중국인의 나머지 정리, 수학, 정수론
'''
E, S, M = map(int, input().split())
e, s, m = E, E, E
year = E
while s != S or m != M:
    s = s + 15 if s + 15 <= 28 else s + 15 - 28
    m = m + 15 if m + 15 <= 19 else m + 15 - 19
    year += 15
print(year)
