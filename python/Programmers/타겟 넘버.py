"""
타겟 넘버
https://programmers.co.kr/learn/courses/30/lessons/43165
깊이우선탐색
풀이1
"""

def dfs(level, total, numbers, target):
    if level == len(numbers):
        if total == target:
            return 1
        return 0
    return dfs(level + 1, total + numbers[level], numbers, target) + dfs(level + 1, total - numbers[level], numbers, target)

def solution(numbers, target):
    return dfs(0, 0, numbers, target)
