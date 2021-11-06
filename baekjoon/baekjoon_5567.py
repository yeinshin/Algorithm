#https://www.acmicpc.net/problem/5567
#5567번-결혼식
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
check = [False]*(n+1)
check[1]=True
ans = []
for _ in range(m):
    a,b = map(int,input().split())
    if a==1: ans.append(b)
    elif b==1: ans.append(a)
    graph[a].append(b)
    graph[b].append(a)

def dfs(cnt,now):
    if cnt == 2:
        if now not in ans :ans.append(now)
        return
    
    for i in graph[now]:
        if not check[i]:
            check[i]=True
            dfs(cnt+1,i)
            check[i]=False
dfs(0,1)
print(len(ans))