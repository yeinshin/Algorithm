#1743번-음식물 피하기

from collections import deque

#n:세로 길이
#m:가로 길이
#k:음식물 쓰레기 수
n,m,k = map(int,input().split())

graph = [[0]*m for _ in range(n)]

#상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(k):
    x,y = map(int,input().split())
    graph[x-1][y-1]=1


def bfs(x,y):
    q=deque()
    q.append((x,y))
    graph[x][y]=0
    count=1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=0 and ny>=0 and nx<n and ny<m:
                if graph[nx][ny]==1:
                    graph[nx][ny]=0
                    q.append((nx,ny))
                    count+=1

    return count

max_trash=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            max_trash=max(max_trash,bfs(i,j))

print(max_trash)