#https://programmers.co.kr/learn/courses/30/lessons/17680
#프로그래머스-캐시

from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0 : return len(cities)*5

    for city in cities:
        city = city.lower()
        if city in cache:
            answer+=1
            cache.remove(city)
            cache.append(city)
        else:    
            answer+=5
            if len(cache)>=cacheSize and cache:
                cache.popleft()
            cache.append(city)
    
    return answer