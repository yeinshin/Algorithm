#프로그래머스-프린터

from collections import deque
def solution(priorities, location):
    answer = 0
    prior = deque([(v,i) for i,v in enumerate(priorities)])
    while prior:
        doc = prior.popleft()
        if prior and doc[0] < max(prior)[0] :
            prior.append(doc)
        else:
            answer+=1
            if doc[1] == location:
                return answer