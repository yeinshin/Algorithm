#https://www.acmicpc.net/problem/14621
#14621번-나만 안되는 연애

n,m = map(int,input().split())
college = ['']+input().split()
edge = list()
parent = list(range(0,n+1))

def find_p(parent,x):
    if parent[x]!=x:
        parent[x]=find_p(parent,parent[x])
    return parent[x]
def union_p(parent,a,b):
    a=find_p(parent,a)
    b=find_p(parent,b)
    if a>b: parent[a]=b
    else: parent[b]=a
for _ in range(m):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))

edge.sort()
result = 0
node = set()
for c,a,b in edge:
    if find_p(parent,a)!=find_p(parent,b) and college[a]!=college[b]:
        union_p(parent,a,b)
        result+=c
        node.add(a)
        node.add(b)
print(result if len(node)==n else -1) 