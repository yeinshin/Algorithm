#https://www.acmicpc.net/problem/13565
#13565번-침투
from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
                board[nx][ny]=2
                q.append((nx,ny))

for j in range(m):
    if board[0][j]==0: bfs(0,j)
    
print('YES' if board[-1].count(2) else 'NO')