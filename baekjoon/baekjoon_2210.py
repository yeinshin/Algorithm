#https://www.acmicpc.net/problem/2210
#2210번-숫자판 점프

graph = [list(input().split()) for _ in range(5)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = set()
def dfs(x,y,s,cnt):
    if cnt == 6:
        result.add(s)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx,ny,s+graph[nx][ny],cnt+1)

for i in range(5):
    for j in range(5):
        dfs(i,j,'',0)
print(len(result))