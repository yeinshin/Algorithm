#https://www.acmicpc.net/problem/4386
#4386번-별자리 만들기
import math
n= int(input())
star = [list(map(float,input().split())) for _ in range(n)]
parent = list(range(n))
edge = list()
for i in range(n-1):
    for j in range(i+1,n):
        edge.append((math.sqrt((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2), i, j))
edge.sort()
def find_p(parent,x):
    if parent[x]!=x:
        parent[x]=find_p(parent,parent[x])
    return parent[x]
def union_p(parent,a,b):
    a=find_p(parent,a)
    b=find_p(parent,b)
    if a>b: parent[a]=b
    else: parent[b]=a
result = 0
for cost,a,b in edge:
    if find_p(parent,a)!=find_p(parent,b):
        union_p(parent,a,b)
        result += cost
print('%.2f'%result)