#https://www.acmicpc.net/problem/13418
#13418번-학교 탐방하기
n,m = map(int,input().split())
result=0
edge=list()
entrance = list(map(int,input().split()))
for _ in range(m):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))

def find_p(parent,x):
    if parent[x]!=x:
        parent[x]=find_p(parent,parent[x])
    return parent[x]
def union_p(parent,a,b):
    a=find_p(parent,a)
    b=find_p(parent,b)
    if a>b:parent[a]=b
    else: parent[b]=a

def union(edge,n):
    road=[0,0]
    road[entrance[-1]]+=1
    parent = list(range(0,n+1))
    for c,a,b in edge:
        if find_p(parent,a)!=find_p(parent,b):
            road[c]+=1
            union_p(parent,a,b)
    return road[0]**2
print(abs(union(sorted(edge),n)-union(sorted(edge,reverse=True),n)))
