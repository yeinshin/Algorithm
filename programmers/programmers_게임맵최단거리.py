#https://programmers.co.kr/learn/courses/30/lessons/1844
#프로그래머스-게임 맵 최단거리

from collections import deque

def bfs(maps,x,y,n,m,visited):
    q = deque()
    q.append((x,y))
    visited[x][y]=1
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1 and visited[nx][ny]==-1:
                visited[nx][ny] = visited[x][y] +1
                q.append((nx,ny))
                
    return visited[n-1][m-1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    
    return bfs(maps,0,0,n,m,visited)