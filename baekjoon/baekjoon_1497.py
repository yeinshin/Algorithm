#https://www.acmicpc.net/problem/1497
#1497번-기타콘서트
from itertools import combinations
n,m = map(int,input().split())
guitar,result = [list(input().split()) for _ in range(n)],[]
for i in range(1,n+1):
    for comb in combinations(range(n),i):
        check = [0]*m
        for j in comb:
            for z in range(m):
                if guitar[j][1][z]=='Y':check[z]=1 
        result.append((check.count(1),i))

ans = sorted(result,key = lambda x: (-x[0],x[1]))
print(ans[0][1] if ans[0][0] else -1)