import heapq


def check(place, x, y):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    min_heap = []
    visited = [[False] * 5 for _ in range(5)]
    heapq.heappush(min_heap, (0, x, y))
    visited[x][y] = True

    while min_heap:
        distance, x, y = heapq.heappop(min_heap)

        if distance and place[x][y] == 'P':
            return False

        if distance >= 2:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or visited[nx][ny]:
                continue
            visited[nx][ny] = True

            if place[nx][ny] == 'X':
                heapq.heappush(min_heap, (distance + 2, nx, ny))
            else:
                heapq.heappush(min_heap, (distance + 1, nx, ny))

    return True


def solution(places):
    answer = []

    for place in places:
        is_valid = True
        for x in range(5):
            for y in range(5):
                if place[x][y] != 'P':
                    continue
                if not check(place, x, y):
                    is_valid = False
                    break
            if not is_valid:
                break

        if is_valid:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))