#https://www.acmicpc.net/problem/14620
#14620번-꽃길

n = int(input())
h = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx,dy = [0,0,0,-1,1],[0,1,-1,0,0]
result = int(1e9)
def check(x,y):
    global n
    for i in range(5):
        nx,ny = x+dx[i],y+dy[i]
        if 0>nx or n<=nx or 0>ny or n<=ny or visited[nx][ny]: return False
    return True
def calc(x,y):
    global n
    cnt = 0
    for i in range(5):
        cnt+=h[dx[i]+x][dy[i]+y]
    return cnt
def dfs(cnt,x,y,cost):
    global result
    if cnt==3:
        result = min(result,cost)
        return
    for i in range(n):
        for j in range(n):
            if check(i,j):
                for b in range(5):
                    visited[dx[b]+i][dy[b]+j]=True
                dfs(cnt+1,i,j,cost+calc(i,j))
                for b in range(5):
                    visited[dx[b]+i][dy[b]+j]=False
dfs(0,0,0,0)
print(result)

