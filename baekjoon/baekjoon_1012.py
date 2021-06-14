#https://www.acmicpc.net/problem/1012
#1012번-유기농 배추

#BFS 풀이
from collections import deque

k = int(input())
result = [0]*k
for i in range(k):
    #NxM, k는 배추가 심어져 있는 위치의 개수
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    where = list()

    for _ in range(k):
        y,x = map(int,input().split())
        graph[x][y] = 1

    def bfs(x,y):
        q = deque()
        q.append((x,y))
        graph[x][y]=1

        while q:
            x,y = q.popleft()
            for z in range(4):
                nx = x + dx[z]
                ny = y + dy[z]

                if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                    graph[nx][ny]=0
                    q.append((nx,ny))
    result=0
    for x in range(n):
        for y in range(m):
            if graph[x][y]==1:
                bfs(x,y)
                result+=1

    print(result)

#------------------------------------------------------------------------------#
#DFS 풀이
k = int(input())
result = [0]*k
for i in range(k):
    #NxM, k는 배추가 심어져 있는 위치의 개수
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    where = list()

    for _ in range(k):
        y,x = map(int,input().split())
        graph[x][y] = 1

    def dfs(x,y):

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=0
                dfs(nx,ny)

    result=0
    for x in range(n):
        for y in range(m):
            if graph[x][y]==1:
                dfs(x,y)
                result+=1

    print(result)