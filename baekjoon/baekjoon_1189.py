#https://www.acmicpc.net/problem/1189
#1189번-컴백홈
r,c,k = map(int,input().split())
home = [list(input()) for _ in range(r)]
dx,dy = [1,-1,0,0],[0,0,-1,1]
result = 0
def dfs(x,y,distance):
    global r,c,k,result
    if x==0 and y==c-1 and k==distance:
        result+=1
        return
    for i in range(4):
        nx,ny = dx[i]+x, dy[i]+y
        if 0<=nx<r and 0<=ny<c and home[nx][ny]=='.':
            home[nx][ny]='T'
            dfs(nx,ny,distance+1)
            home[nx][ny]='.'
home[r-1][0]='T'
dfs(r-1,0,1)
print(result)