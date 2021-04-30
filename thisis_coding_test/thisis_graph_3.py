#2부<문제>3번-도시 분할 계획

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

n,m = map(int,input().split())
parent = [0]*(n+1)

edges = []
result = 0

for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    a,b,cost= map(int,input().split())
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost,a,b = edge

    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        last=cost #마지막 비용은 젤 큰 비용(리스트 edges는 cost의 오름차순으로 정렬되어 있음)

print(result-cost)
    
