#https://www.acmicpc.net/problem/19942
#19942번-다이어트
from itertools import combinations
n = int(input())
target = list(map(int,input().split()))
food = [list(map(int,input().split())) for _ in range(n)]
answer=[]
for i in range(1,n+1):
    for comb in combinations(range(1,n+1),i):
        a,b,c,d,cost = 0,0,0,0,0
        for j in comb:
            a+=food[j-1][0]
            b+=food[j-1][1]
            c+=food[j-1][2]
            d+=food[j-1][3]
            cost+=food[j-1][4]
        if a>=target[0] and b>=target[1] and c>=target[2] and d>=target[3]:
            answer.append((cost,comb))
answer.sort(key = lambda x : (x[0],x[1]))
if answer:print(answer[0][0],' '.join(map(str,answer[0][1])),sep='\n')
else: print(-1)
# print(answer[0][0],' '.join(map(str,answer[0][1])) if answer else -1,sep='\n')
        