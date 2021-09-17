#https://www.acmicpc.net/problem/2660
#2660번-회장뽑기
INF = int(1e9)
n=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]
while True:
    a,b = map(int,input().split())
    if a==-1 and b==-1: break
    graph[a][b]=1
    graph[b][a]=1

for i in range(1,n+1):
    graph[i][i]=0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][b]==1 or graph[a][b]==0:#자기자신이거나 원래 친구인 사이는 건들지 말기
                continue
            else:
                graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

min_value = INF
result = list()
cnt = 0
p = list()
for i in range(1,n+1):
    min_value = min(min_value,max(graph[i][1:]))
    result.append((max(graph[i][1:]),i))
for a,b in sorted(result,key= lambda x:x[1]):
    if a==min_value:
        cnt+=1
        p.append(b)
print(min_value,cnt)
print(' '.join(map(str,p)))


