def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5

    answer = 0
    cache = list()
    cached_cities = set()

    for city in cities:
        city = city.lower()
        cache.append((answer, city))
        if city in cached_cities:
            answer += 1
            continue

        if len(cached_cities) >= cacheSize:
            cache.sort(reverse=True)
            cached_cities.remove(cache.pop()[1])
        cached_cities.add(city)
        answer += 5

    return answer


print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))