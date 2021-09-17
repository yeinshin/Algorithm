#https://www.acmicpc.net/problem/6497
#6497번-전력난

while True:
    m,n= map(int,input().split())
    if m==0 and n==0: break
    
    def find_p(parent,x):
        if parent[x]!=x:
            parent[x]=find_p(parent,parent[x])
        return parent[x]
    
    def union_p(parent,a,b):
        a=find_p(parent,a)
        b=find_p(parent,b)
        if a>b:
            parent[a]=b
        else: parent[b]=a

    parent = list(range(0,m))
    edges = []
    result = 0
    total=0
    for _ in range(n):
        a,b,c = map(int,input().split())
        edges.append((c,a,b))
        total+=c
    edges.sort()
    for cost,a,b in edges:
        if find_p(parent,a)!=find_p(parent,b):
            union_p(parent,a,b)
            result+=cost
    print(total-result)