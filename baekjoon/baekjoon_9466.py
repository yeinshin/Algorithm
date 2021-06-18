#https://www.acmicpc.net/problem/9466
#9466번-텀 프로젝트
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def dfs(now,graph,visited,cycle,result):
    i = graph[now]
    visited[now] = True
    cycle.append(now)
    if not visited[i]:
        dfs(i,graph,visited,cycle,result)
    elif i in cycle:
        result+=cycle[cycle.index(i):]

t = int(input())
for i in range(t):
    n=int(input())
    graph = [0] + list(map(int,input().split()))
    visited = [False]*(n+1)
    result = list()
    for j in range(1,n+1):
        if not visited[j]:
            cycle = list()
            dfs(j,graph,visited,cycle,result)
    print(n-len(set(result)))