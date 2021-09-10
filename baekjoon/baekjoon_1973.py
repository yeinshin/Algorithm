#https://www.acmicpc.net/problem/1937
#1973번-욕심쟁이 판다(풀이 참고함)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,1,-1]
visited = [[0]*n for _ in range(n)]
def dfs(x,y):
    if visited[x][y]: return visited[x][y]
    visited[x][y]=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]>graph[x][y]:
            visited[x][y]=max(visited[x][y],dfs(nx,ny)+1)

    return visited[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer,dfs(i,j))

print(answer)
    