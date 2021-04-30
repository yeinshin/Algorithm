##2부<문제>2번-팀 결성

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a>b:
        parent[b]=a
    else:
        parent[a]=b

#노드와 간선의 수 입력받기
n,m = map(int,input().split())
parent = [0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    check,a,b = map(int,input().split())
    if check==0:
        union_parent(parent,a,b)
    if check==1:
        if find_parent(parent,a)==find_parent(parent,b):
            print("YES")
        else:
            print("NO")
