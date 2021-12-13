#https://www.acmicpc.net/problem/1504
#1504번-특정한 최단 경로(풀이참고)
import heapq
INF = int(1e9)
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())

def dijkstra(start):
    q = []
    distance = [INF]*(n+1)
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        d,now = heapq.heappop(q)
        if distance[now]<d:continue
        for i in graph[now]:
            cost = i[1]+d
            if distance[i[0]]>cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

ans = min(INF,dist_1[v1]+dist_v1[v2]+dist_v2[n],dist_1[v2]+dist_v2[v1]+dist_v1[n])
print(ans if ans!=INF else -1)