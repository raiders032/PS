"""
https://school.programmers.co.kr/learn/courses/30/lessons/64064
불량 사용자
풀이1.100점
"""
import itertools
import re


def solution(user_id, banned_id):
    answer = set()
    patterns = []

    for id in banned_id:
        pattern = ''
        star_count = 0

        for char in id:
            if char != '*':
                if star_count:
                    pattern += f'.{{{star_count}}}'
                    star_count = 0
                pattern += char
                continue
            star_count += 1

        if star_count:
            pattern += f'.{{{star_count}}}'

        patterns.append(pattern)

    for users in itertools.permutations(user_id, len(banned_id)):
        is_valid = True

        for i in range(len(users)):
            if not re.fullmatch(patterns[i], users[i]):
                is_valid = False
                break

        if is_valid:
            answer.add(tuple(sorted(users)))

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
