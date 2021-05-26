#https://www.acmicpc.net/problem/10971
#10971번-외판원 순회2

n=int(input())
cities = [list(map(int,input().split())) for _ in range(n) ]
result = int(1e9)
visited = [False]*n

def dfs(start,cnt,next,cost):
    global result

    if cnt==n:
        if cities[next][start]!=0:
            result = min(result,cost+cities[next][start])
        return
    
    for j in range(n):
        if not visited[j] and cities[next][j]!=0:
            visited[j]=True
            dfs(start,cnt+1,j,cost+cities[next][j])
            visited[j]=False

for i in range(n):
    visited[i]=True
    dfs(i,1,i,0)
    visited[i]=False

print(result)