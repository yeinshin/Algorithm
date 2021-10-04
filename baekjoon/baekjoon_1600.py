#https://www.acmicpc.net/problem/1600
#1600번-말이 되고픈 원숭이(풀이참고)
from collections import deque
k = int(input())
m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

#일반적인 이동
dx = [0,0,-1,1]
dy = [1,-1,0,0]
#말의 이동
hx = [2,2,1,-1,-2,-2,-1,1]
hy = [-1,1,2,2,1,-1,-2,-2]

#3차원 방문 체크 배열
visited = [[[False]*(k+1) for _ in range(m)] for _ in range(n)]

def bfs(x,y):
    q= deque([(x,y,0,0)])
    visited[x][y][0]=True
    while q:
        x,y,skill,cnt = q.popleft()

        #목적지 도착하면 return
        if x==n-1 and y==m-1:
            return cnt
        #일반 이동
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny][skill]==False and graph[nx][ny]==0:
                visited[nx][ny][skill]=True
                q.append((nx,ny,skill,cnt+1))
        #말 이동
        if skill<k:
            for i in range(8):
                nx,ny = x+hx[i],y+hy[i]
                if 0<=nx<n and 0<=ny<m and visited[nx][ny][skill+1]==False and graph[nx][ny]==0:
                    visited[nx][ny][skill+1] = True
                    q.append((nx,ny,skill+1,cnt+1))
    return -1

print(bfs(0,0))