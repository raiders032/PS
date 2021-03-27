"""
https://www.acmicpc.net/problem/1759
1759. 암호 만들기
골드5
백트래킹, 브루트포스, 조합론
풀이2.88ms
"""


def dfs(level, vowel_cnt, password):
    if level == C:
        if len(password) != L or vowel_cnt < 1 or len(password) - vowel_cnt < 2:
            return
        print(password)
        return

    if string[level] in vowels:
        dfs(level + 1, vowel_cnt + 1, password + string[level])
    else:
        dfs(level + 1, vowel_cnt, password + string[level])

    dfs(level + 1, vowel_cnt, password)

vowels = {'a', 'e', 'i', 'o', 'u'}
L, C = map(int, input().split())
string = list(input().split())
string.sort()
dfs(0, 0, '')
