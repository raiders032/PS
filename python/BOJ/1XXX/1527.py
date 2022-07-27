"""
https://www.acmicpc.net/problem/1527
1527.금민수의 개수
풀이1.68ms
"""
def solve(index, number):
    if len(number) == len(str(B)):
        if A <= int(number) <= B:
            return 1
        return 0

    result = 1 if number and A <= int(number) <= B else 0
    result += solve(index + 1, number + '4')
    result += solve(index + 1, number + '7')
    return result


A, B = map(int, input().split())
print(solve(0, ''))