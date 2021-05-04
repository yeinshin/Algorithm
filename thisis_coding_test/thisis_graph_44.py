#3부<문제>2887번-행성 터널

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n=int(input())

parent=[0]*n
edges=[]
planet=[]

for i in range(n):
    parent[i]=i

for _ in range(n):
    x,y,z=map(int,input().split())
    planet.append((x,y,z))

for i in range(n-1):
    for j in range(i+1,n):
        edges.append((min(abs(planet[i][0]-planet[j][0]),abs(planet[i][1]-planet[j][1]),abs(planet[i][2]-planet[j][2])),i,i+1))

edges.sort()

result=0

for edge in edges:
    cost,a,b = edge

    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)