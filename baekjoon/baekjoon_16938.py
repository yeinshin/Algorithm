#https://www.acmicpc.net/problem/16938
#16938번-캠프 준비
from itertools import combinations
N,L,R,X = map(int,input().split())
p = list(map(int,input().split()))
ans = 0
INF = int(1e9)
for i in range(2,N+1):
    for combi in combinations(p,i):
        sum = 0
        minValue,maxValue = INF,-INF
        for c in combi:
            sum+=c
            minValue = min(minValue,c)
            maxValue = max(maxValue,c)
        if L<=sum<=R and (maxValue - minValue)>=X:
            ans+=1
print(ans)