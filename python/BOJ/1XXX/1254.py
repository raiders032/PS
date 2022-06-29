"""
https://www.acmicpc.net/problem/1254
1254.팰린드롬 만들기
실버2
풀이1.76ms
"""
string = input()
string = string[::-1]
length = 1
for i in range(2, len(string) + 1):
    if string[:i] == string[:i][::-1]:
        length = i

if length == len(string):
    print(length)
else:
    extra_number = len(string) - length
    print(length + extra_number * 2)