#https://www.acmicpc.net/problem/20007
#20007번-떡 돌리기
import heapq
n,m,x,y = map(int,input().split())
graph = [[] for _ in range(n)]
INF = int(1e9)
dist = [INF]*n
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
q = []
heapq.heappush(q,(0,y))
dist[y]=0
while q:
    d,now = heapq.heappop(q)
    if dist[now]<d: continue
    for i in graph[now]:
        cost = i[1]+d
        if cost<dist[i[0]]:
            dist[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))
dist.sort()
idx,day,cnt = 1,1,0
while idx<n:
    if dist[idx]*2>x:
        print(-1)
        break
    elif cnt+dist[idx]*2<=x:
        cnt+=dist[idx]*2
    elif cnt+dist[idx]*2>x:
        cnt = dist[idx]*2
        day+=1
    idx+=1
else:print(day)