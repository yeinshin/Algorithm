#DFS 알고리즘 예제 소스코드 

def dfs(graph,v,visited):

    #현재 노드를 방문처리
    visited[v]=True
    print(v,end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

#노드의 수: n
n= int(input())

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[] for _ in range(n+1)]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*(n+1)

dfs(graph,1,visited)