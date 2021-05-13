#2606번-바이러스

#n:컴퓨터 수
n = int(input())

#네트워크 수
m = int(input())

#네트워크 연결 상태를 인접 리스트로 표현
graph = [[] for _ in range(n+1)]

#1번 노드로 부터 연결됐는지 check 해주는 list
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):

    visited[start] = True

    for g in graph[start]:
        if not visited[g]:
            dfs(g)

dfs(1)

result=0
for visit in visited[2:]:
    if visit:
        result+=1

print(result)