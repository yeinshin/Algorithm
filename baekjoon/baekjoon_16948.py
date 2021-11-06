#https://www.acmicpc.net/problem/16948
#16948번-데스 나이트
#N*N 크기의 체스판
from collections import deque
n=int(input())
r1,c1,r2,c2 = map(int,input().split())
graph = [[-1]*n for _ in range(n)]
graph[r1][c1]=0

q = deque([(r1,c1)])
while q:
    r,c = q.popleft()
    if r==r2 and c==c2:
        print(graph[r][c])
        break
    for dr,dc in ((-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)):
        nr = r+dr
        nc = c+dc
        if 0<=nr<n and 0<=nc<n and graph[nr][nc]==-1:
            q.append((nr,nc))
            graph[nr][nc]=graph[r][c]+1
else: print(-1)
