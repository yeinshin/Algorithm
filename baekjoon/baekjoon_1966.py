#https://www.acmicpc.net/problem/1966
#1966번-프린터 큐
from collections import deque
for _ in range(int(input())):
    n,m=map(int,input().split())
    num = list(map(int,input().split()))
    q = deque()
    for i in range(n):
        q.append((i,num[i]))
    cnt =0
    while q:
        t = sorted(q,key = lambda x: -x[1])[0][1]
        i,v = q.popleft()
        if t>v: q.append((i,v))
        else:
            cnt+=1
            if i==m: 
                print(cnt)
                break