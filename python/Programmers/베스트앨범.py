"""
https://programmers.co.kr/learn/courses/30/lessons/42579
베스트앨범
레벨3
자료구조
해시
풀이1
"""
import heapq


def solution(genres, plays):
    answer = []
    genre_dict = dict()

    for index, genre in enumerate(genres):
        if genre not in genre_dict:
            genre_dict[genre] = [plays[index], [(-plays[index], index)]]
        else:
            genre_dict[genre][0] += plays[index]
            heapq.heappush(genre_dict[genre][1], (-plays[index], index))

    genre_list = sorted(genre_dict.items(), key=lambda x: x[1][0], reverse=True)

    for genre in genre_list:
        count = 0
        while genre[1][1] and count < 2:
            song = heapq.heappop(genre[1][1])
            answer.append(song[1])
            count += 1

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
