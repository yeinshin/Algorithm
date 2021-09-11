#https://www.acmicpc.net/problem/17471
#17471번-게리맨더링
from collections import deque
from itertools import combinations

n = int(input())
people =[0]+list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    info = list(map(int,input().split()))
    for j in range(1,len(info)):
        graph[i].append(info[j])

def bfs(array,n):
    visited = [0]*(n+1)
    q = deque([array[0]])
    visited[[array[0]]]=1
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i]==0 and i in array:
                visited[i]=1
                q.append(i)
    return True if sum(visited)==len(array) else False

def total(array):
    t = 0
    for a in array:
        t+=people[a] 
    return t

INF = int(1e9)
result = int(1e9)
a = set(range(1,n+1))
for i in range(1,n//2+1):
    combi = tuple(combinations(range(1,n+1),i))
    for c in combi:
        d =list(a.difference(c))
        if bfs(c,n) and bfs(d,n):
            result=min(result,abs(total(c)-total(d)))

print(result if result!=INF else -1)