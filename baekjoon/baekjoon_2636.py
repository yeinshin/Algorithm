#https://www.acmicpc.net/problem/2636
#2636번-치즈
from collections import deque
n,m = map(int,input().split())
cheese = [[int(m) for m in input().split()] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(visited):
    q = deque([(0,0)])
    visited[0][0] = -1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                if cheese[nx][ny]==1:
                    cheese[nx][ny]=0
                elif cheese[nx][ny]==0:
                    q.append((nx,ny))
                visited[nx][ny]=-1

answer = 0
while True:
    cnt = 0
    for i in range(n):
        cnt += sum(cheese[i])

    if cnt == 0:
        break
    else:
        before = cnt
        answer+=1
        visited = [[0]*m for _ in range(n)]
        bfs(visited)

print(answer)
print(before)