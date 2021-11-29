#https://www.acmicpc.net/problem/17265
#17265번-나의 인생에는 수학과 함께

n = int(input())
graph = [input().split() for _ in range(n)]
visited = [[False]*n for _ in range(n)]
visited[0][0]=True
INF = int(1e9)
min_ans = INF
max_ans = -INF

def calc(c):
    ans = int(c[0])
    for i in range(1,len(c)-1,2):
        if c[i]=='+':ans+=int(c[i+1])
        elif c[i]=='-':ans-=int(c[i+1])
        else: ans*=int(c[i+1])
    return ans

def dfs(x,y,cnt):
    if x==n-1 and y==n-1:
        global min_ans,max_ans
        cost=calc(cnt)
        min_ans,max_ans = min(min_ans,cost),max(max_ans,cost)
        return
    for nx,ny in ((x+1,y),(x,y+1)):
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            visited[nx][ny]=True
            dfs(nx,ny,cnt+graph[nx][ny])
            visited[nx][ny]=False

dfs(0,0,graph[0][0])
print(max_ans,min_ans)