#최대 힙 정렬

import heapq

def heapsort(iterable):
    r = []
    result = []

    for value in iterable:
        heapq.heappush(r,-value)
    
    for _ in range(len(r)):
        result.append(-heapq.heappop(r))

    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)