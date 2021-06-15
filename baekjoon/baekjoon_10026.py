#https://www.acmicpc.net/problem/10026
#10026번-적록색약
#R(빨강), G(초록), B(파랑)
from collections import deque
n = int(input())
grid = [[m for m in input()] for _ in range(n)] #적록색약이 아닌 사람의 그래프
grid_copy = [['']*n for _ in range(n)] #적록색약인 사람의 그래프
for i in range(n):
    for j in range(n):
        if grid[i][j] =='R' or grid[i][j] == 'G':
            grid_copy[i][j]='G'
        else:
            grid_copy[i][j]='B'
    
color = ['R','G','B']
result = [0,0]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,color,graph):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==color:
                graph[nx][ny]='X'
                q.append((nx,ny))
        
#적록색약 아닌 사람
for c in color:
    for a in range(n):
        for b in range(n):
            if grid[a][b]==c:
                bfs(a,b,c,grid)
                result[0]+=1

#적록색약 사람
for c in color[1:]:
    for a in range(n):
        for b in range(n):
            if grid_copy[a][b]==c:
                bfs(a,b,c,grid_copy)
                result[1]+=1

print(*result,sep=' ')