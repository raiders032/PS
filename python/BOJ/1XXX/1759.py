"""
1759. 암호 만들기
골드5
백트래킹, 브루트포스, 조합론
"""

N, M = map(int, input().split())
vowels = {'a', 'e', 'i', 'o', 'u'}
chars = list(input().split())
chars.sort()


def dfs(idx, password, v_num):
    if len(password) == N and v_num >= 1 and len(password) - v_num >= 2:
        print(password)
        return
    for i in range(idx, M):
        if chars[i] in vowels:
            dfs(i + 1, password + chars[i], v_num + 1)
        else:
            dfs(i + 1, password + chars[i], v_num)


dfs(0, '', 0)
