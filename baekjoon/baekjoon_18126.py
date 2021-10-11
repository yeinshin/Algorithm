#https://www.acmicpc.net/problem/18126
#18126번-너구리 구구

#1번 풀이
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
result =0 
def dfs(cnt,now):
    for n,c in graph[now]:
        if visited[n]==-1:
            print('now:',now,'n:',n)
            visited[n]=visited[now]+c
            dfs(cnt+c,n)
            
visited[1]=0
dfs(0,1)
print(max(visited))   


#2번 풀이
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
result =0 
def dfs(cnt,now):
    global result
    result=max(result,cnt)
    visited[now]=True
    for n,c in graph[now]:
        if not visited[n]:
            dfs(cnt+c,n)
            visited[n]=False

# dfs(0,1)
# print(result)