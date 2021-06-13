#https://www.acmicpc.net/problem/2667
#2667번-단지번호붙이기

#DFS 풀이
n=int(input())
town = [[int(i) for i in input()] for _ in range(n)]
visited = [[False]*n for _ in range(n)]
result = [0]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 1

def dfs(x,y):
    global cnt

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<n and 0<=ny<n and town[nx][ny]==1:
            town[nx][ny]=0
            cnt +=1
            dfs(nx,ny)
    return cnt
            

for i in range(n):
    for j in range(n):
        if town[i][j]==1:
            town[i][j]=0
            cnt=1
            result.append(dfs(i,j))
            result[0]+=1
print(result[0])
print(*sorted(result[1:]),sep='\n')

# ----------------------------------------------------------------------------------#
#BFS풀이
from collections import deque

n=int(input())
town = [[int(i) for i in input()] for _ in range(n)]
visited = [[False]*n for _ in range(n)]
result = [0]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,cnt):
    town[x][y]=0
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<n and town[nx][ny]==1:
                town[nx][ny]=0
                q.append((nx,ny))
                cnt+=1
    
    return cnt

for i in range(n):
    for j in range(n):
        if town[i][j]==1:
            result.append(bfs(i,j,1))
            result[0]+=1

print(result[0])
print(*sorted(result[1:]),sep='\n')