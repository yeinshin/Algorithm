#3부<문제>43번-어두운 길
#크루스칼 알고리즘 이용

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

n,m = map(int,input().split())
parent = [0]*(n+1)
edges=[]

for i in range(1,n+1):
    parent[i]=i

#가로등을 다 설치했을 때의 총 금액
money = 0

for _ in range(m):
    x,y,z = map(int,input().split())
    edges.append((z,x,y))
    money+=z

edges.sort()

#최소의 금액으로 활성화 시킬 가로등 비용
result=0

for edge in edges:
    cost,a,b = edge

    if find_parent(parent,a)!=find_parent(parent,b):
        result+=cost
        union_parent(parent,a,b)

#절약한 비용 (총 금액 - 최소 금액)
print(money-result)