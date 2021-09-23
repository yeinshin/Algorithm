#https://www.acmicpc.net/problem/2638
#2638번-치즈
from copy import deepcopy
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
test = deepcopy(graph)
dx,dy=[-1,1,0,0],[0,0,-1,1]
def bfs(x,y):
    pass
cnt = 0
while True: 
    visited = [[False]*m for _ in range(n)]
    cnt+=1

    q = deque([(0,0)])
    visited[0][0]=True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                elif graph[nx][ny]==1:
                    test[nx][ny]+=1
                    if test[nx][ny]>=3: 
                        test[nx][ny]=0
                        visited[nx][ny]=True
    check = False
    for i in range(n):
        for j in range(m):
            if test[i][j]==0 and graph[i][j]!=0: 
                graph[i][j]=0
        if sum(graph[i])!=0: check = True 
    if not check : break

    test = deepcopy(graph)
print(cnt)
    