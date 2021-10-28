#https://programmers.co.kr/learn/courses/30/lessons/87946
#프로그래머스-피로도
from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for comb in permutations(range(len(dungeons)),len(dungeons)):
        test = k
        cnt = 0
        for i in comb:
            if dungeons[i][0]<=test: 
                test-=dungeons[i][1]
                cnt+=1
        answer = max(answer,cnt)
    return answer