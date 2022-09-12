"""
https://school.programmers.co.kr/learn/courses/30/lessons/67258
보석 쇼핑
풀이1.100점
"""
from collections import defaultdict


def solution(gems):
    answer = []
    total_count = len(set(gems))
    gem_count = defaultdict(int)
    gem_count[gems[0]] = 1

    min_length = 100000
    left = 0
    right = 0
    while right < len(gems):
        if len(gem_count) < total_count:
            right += 1
            if right < len(gems):
                gem_count[gems[right]] += 1

        elif len(gem_count) == total_count:
            if right - left < min_length:
                min_length = right - left
                answer = [left + 1, right + 1]

            gem_count[gems[left]] -= 1
            if gem_count[gems[left]] == 0:
                del gem_count[gems[left]]
            left += 1

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
