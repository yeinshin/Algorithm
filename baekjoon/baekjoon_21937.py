#https://www.acmicpc.net/problem/21937
#21937번-작업(풀이참고)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
end = int(input())
result = 0
visited = [False]*(n+1)
q=[end]
while q:
    target = q.pop()
    for i in graph[target]:
        if not visited[i]:
            visited[i]=True
            result+=1
            q.append(i)
print(result)

