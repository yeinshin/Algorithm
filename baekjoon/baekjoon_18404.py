#https://www.acmicpc.net/problem/18404
#18404번-현명한 나이트
from collections import deque
n,m = map(int,input().split())
x,y = map(int,input().split())
graph = [[-1]*n for _ in range(n)]
mal = [list(map(int,input().split())) for _ in range(m)]

q = deque([(x-1,y-1)])
graph[x-1][y-1]=0
while q:
    X,Y = q.popleft()
    for nx,ny in ((X-2,Y-1), (X-2,Y+1), (X-1,Y-2), (X-1,Y+2), (X+1,Y-2), (X+1,Y+2), (X+2,Y-1), (X+2,Y+1)):
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==-1:
                q.append((nx,ny))
                graph[nx][ny]=graph[X][Y]+1
for a,b in mal:
    print(graph[a-1][b-1],end=' ')