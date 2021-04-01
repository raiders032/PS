"""
https://programmers.co.kr/learn/courses/30/lessons/42840
모의고사
레벨1
완전탐색
풀이1
"""

def solution(answers):
    scores = [0, 0, 0]
    patterns_1 = [1, 2, 3, 4, 5]
    patterns_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    patterns_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for index, answer in enumerate(answers):
        scores[0] += 1 if patterns_1[index % 5] == answer else 0
        scores[1] += 1 if patterns_2[index % 8] == answer else 0
        scores[2] += 1 if patterns_3[index % 10] == answer else 0

    res = []
    max_score = max(scores)
    for i in range(3):
        if max_score == scores[i]:
            res.append(i + 1)
    return res

print(solution([1, 2, 3, 4, 5]))

"""
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
"""