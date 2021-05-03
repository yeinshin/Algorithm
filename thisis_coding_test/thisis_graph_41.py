#3부<문제>41번-여행 계획

#n: 여행지의 수, m: 여행 계획에 속한 도시의 수
n,m = map(int,input().split())

#두 여행지의 연결 여부
travel=[[int(m) for m in input().split()] for _ in range(n)]

#여행계획에 포함된 여행지의 번호들
dst = list(map(int,input().split()))

#루트 노드 정보를 저장할 리스트
parent = [0]*(n+1)

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(1,n+1):
    parent[i]=i

for a in range(n):
    for b in range(n):
        if travel[a][b]==1:
            union_parent(parent,a+1,b+1)

dst = set(dst)
dst = list(dst)

cycle = True

for d in range(m-1):
    if parent[dst[d]]!=parent[dst[d+1]]:
        #하나라도 루트 노드가 서로 다르면 False를 반환
        cycle = False

if cycle:
    print("YES")
else:
    print("NO")








