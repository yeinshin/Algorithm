#https://www.acmicpc.net/problem/15900
#15900번-나무 탈출
from collections import defaultdict
n = int(input())
graph = [[] for _ in range(n+1)]
cnt = defaultdict(int)
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    cnt[a]+=1
    cnt[b]+=1
visited = [False]*(n+1)
visited[1]=True
print(cnt)
def dfs(now):

    for i in graph[now]:
        if not visited[i]:
            print('i:',i)
            visited[i]=True
            dfs(i)
    print('리프노드:',now)

dfs(1)