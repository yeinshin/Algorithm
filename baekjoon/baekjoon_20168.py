#https://www.acmicpc.net/problem/20168
#20168번-골목 대장 호석 - 기능성

import sys
input = sys.stdin.readline
n,m,a,b,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
visited[a]=1
for _ in range(m):
    i,j,z = map(int,input().split())
    graph[i].append((j,z))
    graph[j].append((i,z))
ans = []
def dfs(start,end,cnt,maxcost):
    if start == end:
        ans.append((maxcost,cnt))
        return
    for i in graph[start]:
        if not visited[i[0]]:
            visited[i[0]]=1
            if i[1]>maxcost:dfs(i[0],end,cnt+i[1],i[1])
            else:dfs(i[0],end,cnt+i[1],maxcost)
            visited[i[0]]=0
dfs(a,b,0,0)
ans.sort()
for i,j in ans:
    if j<=c: 
        print(i)
        break
else: print(-1)