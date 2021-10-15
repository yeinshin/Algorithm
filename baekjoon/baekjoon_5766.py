#https://www.acmicpc.net/problem/5766
#5766번-할아버지는 유명해!
from collections import defaultdict
while 1:
    n,m=map(int,input().split())
    if n==0 and m==0: break
    score = defaultdict(int)
    result = list()
    for i in range(n):
        seonsu = list(map(int,input().split()))
        for s in seonsu:
            score[s]+=1
    second = sorted(score.values(),reverse= True)[1]
    for i,v in score.items():
        if v==second: result.append(i)
    print(*sorted(result),sep=' ')
