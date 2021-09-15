#https://www.acmicpc.net/problem/14496
#14496번-그대,그머가 되어
import heapq
a,b = map(int,input().split())
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append((y,1))
    graph[y].append((x,1))
INF = int(1e9)
dist = [INF]*(n+1)
q = []
heapq.heappush(q,(0,a))
dist[a]=0
while q:
    d,now = heapq.heappop(q)
    if dist[now]<d:
        continue
    for i in graph[now]: #i[0]:노드번호, i[1]:비용
        cost = i[1]+d
        if cost<dist[i[0]]:
            dist[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))
print( dist[b] if dist[b]!=INF else -1)