#https://www.acmicpc.net/problem/16234
#16234번-인구 이동(풀이참고함)
from collections import deque
import sys
input = sys.stdin.readline

n,l,r = map(int,input().split())
land = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    q = deque([(i,j)])
    visited[i][j] = 1
    temp = list()
    temp.append([i,j])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if l<=abs(land[x][y]-land[nx][ny])<=r:
                    visited[nx][ny]=1
                    temp.append((nx,ny))
                    q.append((nx,ny))
    return temp

answer = 0
while True:
    visited = [[0]*n for _ in range(n)]
    flag = False #연합이 일어났는지 check
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                temp = bfs(i,j)
                if len(temp)>1: # 연합이 일어났다면
                    flag = True
                    num = sum(land[x][y] for x,y in temp)//len(temp)
                    for x,y in temp:
                        land[x][y] = num
    if not flag: break
    answer+=1
    
print(answer)