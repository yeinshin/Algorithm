#https://www.acmicpc.net/problem/12761
#12761번-돌다리
from collections import deque
a,b,x,y = map(int,input().split())
visited = [0]*100001
dx = [-1,1,a,-a,b,-b,a,b]

q = deque([x])
visited[x]=0
while q:
    x = q.popleft()
    if x==y:
        print(visited[y])
        break
    for i in range(8):
        if i<6:
            nx = dx[i]+x
            if 0<=nx<100001 and visited[nx]==0:
                visited[nx]=visited[x]+1
                q.append(nx)
        else:
            nx = dx[i]*x
            if 0<=nx<100001 and visited[nx]==0:
                visited[nx]=visited[x]+1
                q.append(nx)