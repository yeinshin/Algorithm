#https://www.acmicpc.net/problem/11581
#11581번-구호물자(풀이참고)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(1,n):
    m = int(input())
    c = list(map(int,input().split()))
    for j in c:
        graph[i].append(j)
print('graph:',graph)
def dfs(start):
    for i in graph[start]:
        print('i:',i)
        if visited[i]:
            return True
        visited[i] = True
        if dfs(i):
            return True
        visited[i] = False
    return False
print('CYCLE' if dfs(1) else 'NO CYCLE')