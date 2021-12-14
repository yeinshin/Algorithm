#https://www.acmicpc.net/problem/1303
#1303번-전쟁-전투

from collections import deque

#n:전쟁터의 가로크기
#m:전쟁터의 세로크기
n,m = map(int,input().split())

#병사들의 배치
#B:파랑, W:흰색
graph = [list(input()) for _ in range(m)]

#상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,color,color_type):
    q=deque()
    q.append((x,y))
    graph[x][y]=color_type

    power = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx>=0 and ny>=0 and nx<m and ny<n:
                if graph[nx][ny]==color:
                    graph[nx][ny]=color_type
                    q.append((nx,ny))
                    power+=1

    return power**2

white = 0
blue = 0

for i in range(m):
    for j in range(n):
        if graph[i][j]=='W':
            white+=bfs(i,j,'W',0)

        elif graph[i][j]=='B':
            blue+=bfs(i,j,'B',1)

print(white,blue,end ='\n\n')
