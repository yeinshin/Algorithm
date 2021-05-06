#18352번-특정 거리의 도시 찾기
#3부<문제>15번-특정 거리의 도시 찾기

from collections import deque
import sys

#n: 도시의 개수
#m: 도로의 개수
#k: 거리 정보
#x: 출발 도시의 번호
n,m,k,x = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)


def bfs (start):
    q=deque([start])
    visited[start]=0

    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if visited[i]==-1:
                visited[i]=visited[now]+1
                q.append(i)
                
bfs(x)
check = False

for i in range(1,n+1):
    if visited[i]==k:
        print(i)
        check = True #거리가 k인 노드가 하나라도 존재함

if not check:
    print('-1')