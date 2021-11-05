#https://www.acmicpc.net/problem/18232
#18232번-텔레포트 정거장
from collections import deque
#n:1-n점 , m:텔레포트 개수
n,m = map(int,input().split())
#주예 위치: S, 방주 위치:E
s,e = map(int,input().split())
dx = [-1,1]
visited = [-1]*300001
tele = [[] for _ in range(300001)]
for _ in range(m):
    a,b = map(int,input().split())
    tele[a].append(b)
    tele[b].append(a)
q = deque([s])
visited[s]=0
while q:
    x = q.popleft()
    if x==e:
        print(visited[e])
        break
    if tele[x]:
        for k in tele[x]:
            if visited[k]==-1:
                q.append(k)
                visited[k]=visited[x]+1
    for i in range(len(dx)):
        nx = x+dx[i]
        if 0<=nx<300001 and visited[nx]==-1:
            q.append(nx)
            visited[nx]=visited[x]+1