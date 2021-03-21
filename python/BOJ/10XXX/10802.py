# 10802번 문자열 분석 브론즈2
import sys
while True:
    line = sys.stdin.readline().rstrip('\n')
    if not line:
        break
    count = [0]*4
    for x in line:
        if 0 <= (ord(x) - ord('a')) < 26:
            count[0] += 1
        elif 0 <= (ord(x) - ord('A')) < 26:
            count[1] += 1
        elif 0 <= (ord(x) - ord('0')) < 10:
            count[2] += 1
        elif x == ' ':
            count[3] += 1
    for x in count:
        print(x, end=' ')
    print()
