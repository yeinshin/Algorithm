#https://www.acmicpc.net/problem/2224
#2224번-명제 증명
n = int(input())
x = []
member = set()
info = dict()
for _ in range(n):
    a = input().split(' ')
    x.append((a[0],a[2]))
    member.add(a[0])
    member.add(a[2])
member = sorted(member)
m = len(member)
for i in range(m):
    info[member[i]]=i

INF = int(1e9)
floyd = [[INF]*m for _ in range(m)]
for a,b in x:
    floyd[info[a]][info[b]]=1

for k in range(m):
    for a in range(m):
        for b in range(m):
            floyd[a][b]=min(floyd[a][b],floyd[a][k]+floyd[k][b])
result = []
for i in range(m):
    for j in range(m):
        if floyd[i][j]!=INF and i!=j:
            result.append('%s => %s'%(member[i],member[j]))

print(len(result))
print(*result,sep='\n')