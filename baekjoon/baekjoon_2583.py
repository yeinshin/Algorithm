#https://www.acmicpc.net/problem/2583
#2583번-영역 구하기
from collections import deque
#눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이
#k개의 직사각형
m,n,k = map(int,input().split())
graph = [[0]*n for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=1

def bfs(i,j):
    global cnt

    q = deque()
    q.append((i,j))
    graph[i][j]=1
    cnt+=1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
                graph[nx][ny]=1
                cnt+=1
                q.append((nx,ny))
    return cnt

result=0
w = list()
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            cnt=0
            result+=1
            w.append(bfs(i,j))
print(result)
print(*sorted(w),sep=' ')