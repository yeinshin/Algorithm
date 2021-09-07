#https://www.acmicpc.net/problem/3187
#3187번-양치기 꿍
from collections import deque
r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
def bfs(x,y):
    global sheep,wolf
    q=deque([(x,y)])
    visited[x][y]=True
    while q:
        x,y = q.popleft()
        if graph[x][y]=='v':wolf+=1
        elif graph[x][y]=='k':sheep+=1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y 
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and graph[nx][ny]!='#':
                visited[nx][ny]=True
                q.append((nx,ny))
s,w = 0,0
for i in range(r):
    for j in range(c):
        if graph[i][j]!='#' and not visited[i][j]:
            sheep,wolf=0,0
            bfs(i,j)
            if sheep>wolf: s+=sheep
            else: w+=wolf
print(s,w)