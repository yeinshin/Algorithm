#https://programmers.co.kr/learn/courses/30/lessons/68646
#프로그래머스-풍선 터트리기/풀이 참고함
import heapq
def solution(a):
    answer = 1
    min_heap = []
    
    idx = a.index(min(a))
    left = a[:idx]
    right = reversed(a[idx+1:])
    
    for v in left:
        heapq.heappush(min_heap,v)
        if min_heap[0] == v:
            answer +=1
    
    min_heap = []
    for v in right:
        heapq.heappush(min_heap,v)
        if min_heap[0] == v:
            answer +=1
        
    
    return answer