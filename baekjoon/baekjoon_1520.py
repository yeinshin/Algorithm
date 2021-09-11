#https://www.acmicpc.net/problem/1520
#1520번-내리막 길/DP로 풀어야함(풀이참고함)
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x==n-1 and y==m-1: return 1
    if visited[x][y]!=-1 : return visited[x][y]
    visited[x][y]=0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]<graph[x][y]:
            visited[x][y]+=dfs(nx,ny)
    return visited[x][y]

print(dfs(0,0))