#https://www.acmicpc.net/problem/21735
#21735번-눈덩이 굴리기
n,m = map(int,input().split())
yard = list(map(int,input().split()))
visited = [0]*n
ans = 0
dx = [1,2]
def dfs(cnt,x,size):
    if cnt==m or x==n-1:
        global ans
        ans = max(ans,size)
        return
    
    for i in range(2):
        nx = dx[i]+x
        if 0<=nx<n and not visited[nx]:
            visited[nx]=1
            if i==0:dfs(cnt+1,nx,size+yard[nx])
            else: dfs(cnt+1,nx,size//2+yard[nx])
            visited[nx]=0
dfs(0,-1,1)
print(ans)