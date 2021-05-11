#프로그래머스-네트워크
#Union-Find 풀이

from collections import Counter

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
        
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

def solution(n, computers):
    
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                union_parent(parent,i,j)
                
    answer = set()
    for i in range(n):
        parent[i] = find_parent(parent, i)
        answer.add(parent[i])

    print("set(parent):",set(parent),end="\n\n")
    print("parent:",parent,end="\n\n")
    print("answer:",answer)
    
    return len(answer)
