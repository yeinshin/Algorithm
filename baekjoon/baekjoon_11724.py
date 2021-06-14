#https://www.acmicpc.net/problem/11724
#11724번-연결 요소의 개수
#(연결 요소의 개수 문제는 BFS, DFS 문제로 보통은 풀지만 유니온파인드를 사용할 수 있습니다. )

#DFS 풀이(연결리스트 이용)
n,m = map(int,input().split())
edges = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

def dfs(start,cnt):

    for i in edges[start]:
        if visited[i]!=cnt:
            visited[i]=cnt
            dfs(i,cnt)

cnt=0
for i in range(1,n+1):
    if visited[i]==0:
        cnt+=1
        dfs(i,cnt)
        if visited[i]==0:
            visited[i]=i

print(len(set(visited[1:])))

#---------------------------------------------------------------------------------#
#유니온파인드(Union-Find) 풀이
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

#정점: n
#간선: m
n,m = map(int,input().split())
parent = [0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

for i in range(1,n+1):
    find_parent(parent,i)

print(len(set(parent[1:])))
    

