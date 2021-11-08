#https://www.acmicpc.net/problem/17141
#17141번-연구소 2
from collections import deque
from itertools import combinations
INF = int(1e9)
n,m = map(int,input().split())
labor = [list(map(int,input().split())) for _ in range(n)]
birus = []
q = deque()
one = 0
for i in range(n):
    for j in range(n):
        if labor[i][j]==2: birus.append((i,j))
        elif labor[i][j]==1: one+=1

def bfs(n,INF,one):
    while q:
        x,y = q.popleft()
        for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1 and labor[nx][ny]!=1:
                visited[nx][ny] = visited[x][y]+1
                check[nx][ny]=0
                q.append((nx,ny))
    c = 0
    time = -1
    for i in range(n):
        c+=sum(check[i])
        time = max(time,max(visited[i]))
    return time if c==one else INF

ans = INF
for comb in combinations(birus,m):
    visited = [[-1]*n for _ in range(n)]
    check = [[1]*n for _ in range(n)]
    for a,b in comb:
        q.append((a,b))
        visited[a][b]=0
        check[a][b]=0
    ans = min(ans,bfs(n,INF,one))

print(ans if ans!=INF else -1)