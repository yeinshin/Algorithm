#https://www.acmicpc.net/problem/21938
#21938번-영상처리
from collections import deque
n,m = map(int,input().split())
first = [list(map(int,input().split())) for _ in range(n)]
t = int(input())
result = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(0,m*3,3):
        if t<=sum(first[i][j:j+3])//3:result[i][j//3]=255

def bfs(x,y):
    dx,dy=[0,0,-1,1],[1,-1,0,0]
    q=deque([(x,y)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<m and result[nx][ny]==255:
                q.append((nx,ny))
                result[nx][ny]=0

cnt = 0
for i in range(n):
    for j in range(m):
        if result[i][j]==255:
            bfs(i,j)
            cnt+=1
print(cnt)