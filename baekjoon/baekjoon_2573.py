#https://www.acmicpc.net/problem/2573
#2573번-빙산

from collections import deque
from copy import deepcopy

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
melting = deepcopy(graph)
dx,dy = [-1,1,0,0],[0,0,-1,1]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]!=0:
                q.append((nx,ny))
                visited[nx][ny]=True
time = 0
while True:
    time +=1
    for x in range(n):
        for y in range(m):
            cnt = 0
            if graph[x][y]!=0:
                for a in range(4):
                    nx = dx[a] + x
                    ny = dy[a] + y
                    if 0<=nx<n and 0<=ny<m and not graph[nx][ny]:
                        cnt +=1
                melting[x][y] = 0 if melting[x][y]-cnt<0 else melting[x][y]-cnt
    
    graph = deepcopy(melting)
    visited = [[False]*m for _ in range(n)]
    ice = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]!=0:
                bfs(i,j)
                ice+=1
    if ice>=2:
        print(time)
        break
    if ice==0:
        print(0)
        break

