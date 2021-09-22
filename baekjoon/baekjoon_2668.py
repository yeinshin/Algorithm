#https://www.acmicpc.net/problem/2668
#2668번-숫자고르기(풀이참고)

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    graph[i].append(int(input()))
def dfs(n,start):
    visited[n]=True
    for i in graph[n]:
        if not visited[i]:
            dfs(i,start)
        elif visited[i] and i==start:
            answer.append(i)
answer = []
for i in range(1,n+1):
    visited = [False]*(n+1)
    dfs(i,i)
print(len(answer))
print(*answer,sep='\n')
