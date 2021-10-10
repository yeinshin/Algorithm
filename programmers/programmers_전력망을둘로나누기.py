#https://programmers.co.kr/learn/courses/30/lessons/86971
#프로그래머스-전력망을 둘로 나누기
from collections import Counter
def solution(n, wires):
    answer = int(1e9)
    def find_parent(x,parent):
        if parent[x]!=x: parent[x]=find_parent(parent[x],parent)
        return parent[x]
    def union_find(a,b,parent):
        a=find_parent(a,parent)
        b=find_parent(b,parent)
        if a>b: parent[a]=b
        else: parent[b]=a

    for i in range(len(wires)):
        parent = list(range(n+1))
        for j in range(len(wires)):
            if j==i:continue
            a,b = wires[j]
            union_find(a,b,parent)
        for m in range(1,n+1):
            parent[m] = find_parent(m,parent)
        cnt_p = Counter(parent[1:])
        if len(cnt_p)==2:
            v=list(cnt_p.values())
            answer = min(answer,abs(v[0]-v[1]))
    return answer