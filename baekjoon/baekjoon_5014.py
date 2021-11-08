#https://www.acmicpc.net/problem/5014
#5014번-스타트링크
from collections import deque
f,s,g,u,d = map(int,input().split())
floor = [-1]*(f+1)

q = deque([s])
floor[s]=0
while q:
    x = q.popleft()
    if x==g:
        print(floor[x])
        break
    for nx in ((x+u),(x-d)):
        if 0<nx<=f and floor[nx]==-1:
            floor[nx]=floor[x]+1
            q.append(nx)
else: print("use the stairs")