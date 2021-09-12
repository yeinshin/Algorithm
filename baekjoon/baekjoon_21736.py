#https://www.acmicpc.net/problem/21736
#21736번-헌내기는 친구가 필요해
#O는 빈 공간, X는 벽, I는 도연이, P는 사람
from collections import deque
n,m = map(int,input().split())
campus = [list(input()) for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
answer = 0
def bfs(x,y):
    global answer
    q = deque([(x,y)])
    campus[x][y]='x'
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and campus[nx][ny]!='X':
                if campus[nx][ny]=='P': answer+=1
                q.append((nx,ny))
                campus[nx][ny]='X'
for i in range(n):
    for j in range(m):
        if campus[i][j]=='I':
            bfs(i,j)
            break

print(answer if answer else 'TT')