#https://www.acmicpc.net/problem/18223
#18223번-민준이와 마산 그리고 건우
import heapq
INF = int(1e9)
v,e,p = map(int,input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    dist = [INF]*(v+1)
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        d,now = heapq.heappop(q)
        if dist[now]<d:continue
        for i in graph[now]:
            cost = d+i[1]
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return dist

dist_1 = dijkstra(1)
dist_p = dijkstra(p)
print("SAVE HIM" if dist_1[v]>=dist_1[p]+dist_p[v] else "GOOD BYE" )