#https://www.acmicpc.net/problem/2422
#2422번-한윤정이 이탈리아에 가서 아이스크림을 사먹는데
from itertools import combinations
n,m = map(int,input().split())
ice = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    ice[a].append(b)
    ice[b].append(a)
result =0 
for a,b,c in combinations(range(1,n+1),3):
    if b not in ice[a] and c not in ice[a] and c not in ice[b]: result +=1
print(result)
