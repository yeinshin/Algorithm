#https://www.acmicpc.net/problem/7576
#7576번-토마토

from collections import deque

#NxM
m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()

def bfs():
    # q = deque()
    # q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                q.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append((i,j))

bfs()

result = 0
for i in range(n):
    if graph[i].count(0)>=1:
        result = -1
        break
    else:
        result=max(result,max(graph[i])-1)
print(result)