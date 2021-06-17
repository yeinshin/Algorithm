#https://www.acmicpc.net/problem/1922
#1922번-네트워크 연결

#각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라. 
# -> 최소스패닝 알고리즘 이용 (크루스칼 알고리즘)

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

#컴퓨터의 수
n = int(input())
#연결할 수 있는 선의 수
m = int(input())
parent = list(range(0,n+1))
print(parent)
edges = list()
result = 0

for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort() 

for cost,a,b in edges:
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)



