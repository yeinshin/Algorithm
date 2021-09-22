#https://www.acmicpc.net/problem/16432
#16432번-떡장수와 호랑이
import sys
n = int(input())
dduck = [[] for _ in range(n+1)]
visited = [[False]*10 for _ in range(n+1)]
for i in range(1,n+1):
    d = list(map(int,input().split()))
    dduck[i].extend(d[1:])
def dfs(n,end,before,eat):
    if n == end+1:
        for i in eat:
            print(i)
        sys.exit()
    for i in dduck[n]:
        if before!=i and not visited[n][i]:
            visited[n][i]=True
            dfs(n+1,end,i,eat+[i])
dfs(1,n,0,[])
print(-1)