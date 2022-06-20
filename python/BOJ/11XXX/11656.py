"""
https://www.acmicpc.net/problem/11656
11656.접미사 배열
실버4
풀이1.76ms
"""
string = input()
words = []
for i in range(len(string)):
    words.append(string[i:])

words.sort()
for word in words:
    print(word)