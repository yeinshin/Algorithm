#https://programmers.co.kr/learn/courses/30/lessons/12979
#프로그래머스-기지국 설치/정확성 테스트는 통과하였으나, 효율성에서 실패하여 풀이 참고함
from math import ceil

def solution(n, stations, w):
    answer = 0
    nonstation = [(0,0)]
    
    for station in stations:
        left = station - w if station - w>=0 else 0
        right = station + w if station + w <=n else n
        nonstation.append((left,right))
    nonstation.append((n+1,n+1))
    
    for i in range(len(nonstation)-1):
        answer += ceil((nonstation[i+1][0] - nonstation[i][1]-1) / (w*2+1)) 

    return answer