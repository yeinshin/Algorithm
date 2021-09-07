#https://www.acmicpc.net/problem/3184
#3184번-양
from collections import deque

n,m = map(int,input().split())
ground = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global sheep,wolf
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        if ground[x][y]=='v': wolf+=1
        elif ground[x][y]=='o':sheep+=1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and ground[nx][ny]!='#':
                visited[nx][ny]=True
                q.append((nx,ny))

s,w = 0,0
for i in range(n):
    for j in range(m):
        if ground[i][j]!='#' and not visited[i][j]:
            sheep, wolf = 0,0
            bfs(i,j)
            if sheep>wolf : s+=sheep
            else: w+=wolf

print(s,w)

