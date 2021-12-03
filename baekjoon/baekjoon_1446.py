#https://www.acmicpc.net/problem/1446
#1446번-지름길
import sys
input = sys.stdin.readline
n,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dist = [i for i in range(d+1)]
ans = 0
for i in range(1,d+1):
    dist[i]=min(dist[i],dist[i-1]+1)
    for a,b,c in graph:
        if b==i and dist[a]+c<dist[b]:dist[b]=dist[a]+c
print(dist[d])


