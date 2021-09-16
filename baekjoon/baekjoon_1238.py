#https://www.acmicpc.net/problem/1238
#1238번-파티

import heapq
n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
def dijkstra(start,x):
    q = []
    heapq.heappush(q,(0,start))
    distance = [int(1e9)]*(n+1)
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = i[1]+dist
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance[x]
result = 0
for i in range(1,n+1):
    result=max(result,dijkstra(i,x)+dijkstra(x,i))
print(result)