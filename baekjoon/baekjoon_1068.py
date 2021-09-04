#https://www.acmicpc.net/problem/1068
#1068번-트리

n = int(input())
tree = list(map(int,input().split()))
delete = int(input())

graph = [[] for _ in range(n)]
answer = 0

for i in range(n):
    if tree[i]==-1:
        rootnode = i
        continue
    if i==delete:
        continue
    graph[tree[i]].append(i)

def dfs(start):
    global answer

    if not graph[start]: #즉 리프노드에 도달하면 answer에 1을 추가
        answer+=1
        return
    for i in graph[start]:
        dfs(i)

if rootnode!=delete:
    dfs(rootnode)

print(answer)