#https://programmers.co.kr/learn/courses/30/lessons/85002
#프로그래머스-복서 정렬하기(위클리 챌린지)
def solution(weights, head2head):
    answer, info = [],[]
    n = len(weights)
    for i in range(n):
        big,fight,win = 0,0,0
        for j in range(n):
            if head2head[i][j]!='N':
                if head2head[i][j]=='W':
                    if weights[i]<weights[j]: big+=1
                    win+=1
                fight +=1
        # #승률, 자신보다 몸무게가 무거운 복서를 이긴 횟수, 자기 몸무게,번호
        info.append((win/fight*100,big,weights[i],i) if win>0 else (0,big,weights[i],i))
        
    info = sorted(info,key = lambda x: (x[0],x[1],x[2],-x[3]),reverse = True)
    return [info[i][-1]+1 for i in range(n)]